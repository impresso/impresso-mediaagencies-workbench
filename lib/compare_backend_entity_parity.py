"""Entity-level parity check between an external inference backend and the evaluator.

The model-inference parity check (`compare_model_inference_parity`) compares
token label sequences of the Hugging Face pipeline. External corpus backends,
such as `impresso-inference`, emit character-offset entities instead, so this
module compares at the entity level:

1. `export-input` writes the release test split as Impresso-style JSONL
   (`id`, `ft`, `d`) that a backend can read. With `--concat-size N > 1`,
   consecutive documents are joined into longer synthetic documents, which
   exposes truncation and windowing errors that short test snippets hide.
   A manifest records where each source document starts.
2. `reference-run` runs the verified Hugging Face pipeline (`pipeline.py` of a
   downloaded model directory) on the same backend input and writes its
   entities in backend format. Use it as the reference for concatenated input:
   windows then span document boundaries, so per-document evaluator
   predictions are no longer the exact expected output.
3. `compare` reads the backend output (`id`, `entities[{label, offset}]`) and
   compares it with the reference: the evaluator's decoded predictions mapped
   to character offsets, or a `reference-run` output. It reports per-document
   parity, mismatch categories, and entity metrics against gold for both.

Run the backend with anachronism filtering disabled; the evaluator does not
filter by publication year.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from lib.compare_model_inference_parity import labels_to_entities

DOC_SEPARATOR = "\n\n"

Span = tuple[int, int, str]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def token_spans_to_char_spans(spans: set[tuple[int, int, str]], row: dict[str, Any], shift: int = 0) -> set[Span]:
    starts = row["token_start_offsets"]
    stops = row["token_end_offsets"]
    return {(starts[s] + shift, stops[e - 1] + shift, label) for s, e, label in spans}


def gold_char_spans(row: dict[str, Any], shift: int = 0) -> set[Span]:
    return {(e["start"] + shift, e["stop"] + shift, e["label"]) for e in row.get("entities") or []}


def build_groups(rows: list[dict[str, Any]], concat_size: int) -> list[dict[str, Any]]:
    """Group consecutive documents into synthetic documents with member offsets."""
    groups: list[dict[str, Any]] = []
    for index in range(0, len(rows), concat_size):
        members = rows[index : index + concat_size]
        if concat_size == 1:
            group_id = members[0]["id"]
        else:
            group_id = f"concat-{index // concat_size:05d}"
        parts: list[str] = []
        offsets: list[dict[str, Any]] = []
        cursor = 0
        for member in members:
            if parts:
                parts.append(DOC_SEPARATOR)
                cursor += len(DOC_SEPARATOR)
            offsets.append({"id": member["id"], "offset": cursor})
            parts.append(member["text"])
            cursor += len(member["text"])
        groups.append({"id": group_id, "text": "".join(parts), "date": members[0].get("date") or "", "members": offsets})
    return groups


def export_input(args: argparse.Namespace) -> int:
    rows = load_jsonl(args.input_jsonl)
    groups = build_groups(rows, args.concat_size)
    write_jsonl(args.output_jsonl, [{"id": g["id"], "ft": g["text"], "d": g["date"][:10]} for g in groups])
    write_json(args.manifest_json, {"concat_size": args.concat_size, "source": str(args.input_jsonl), "groups": [
        {"id": g["id"], "members": g["members"], "chars": len(g["text"])} for g in groups
    ]})
    print(f"Wrote {len(groups)} backend input documents from {len(rows)} test documents to {args.output_jsonl}")
    return 0


def reference_run(args: argparse.Namespace) -> int:
    from lib.compare_model_inference_parity import import_pipeline, import_runtime

    AutoModelForTokenClassification, AutoTokenizer = import_runtime()
    MediaAgenciesPipeline = import_pipeline(args.model_dir)
    tokenizer = AutoTokenizer.from_pretrained(str(args.model_dir))
    model = AutoModelForTokenClassification.from_pretrained(str(args.model_dir))
    model.eval()
    pipeline = MediaAgenciesPipeline(model, tokenizer)
    out = []
    for row in load_jsonl(args.backend_input):
        result = pipeline.predict_one(row["ft"])
        out.append({"id": row["id"], "entities": [
            {"label": e["label"], "offset": [e["start"], e["stop"]]} for e in result.get("entities", [])
        ]})
    write_jsonl(args.output_jsonl, out)
    print(f"Wrote reference pipeline entities for {len(out)} documents to {args.output_jsonl}")
    return 0


def backend_char_spans(row: dict[str, Any]) -> set[Span]:
    spans: set[Span] = set()
    for entity in row.get("entities") or []:
        start, stop = entity["offset"]
        spans.add((int(start), int(stop), entity["label"]))
    return spans


def classify(expected: set[Span], actual: set[Span]) -> Counter[str]:
    """Count mismatch categories between two entity sets."""
    counts: Counter[str] = Counter()
    missing = expected - actual
    extra = actual - expected
    matched_extra: set[Span] = set()
    for start, stop, label in sorted(missing):
        overlap = [x for x in extra if x[0] < stop and start < x[1] and x not in matched_extra]
        same_span = [x for x in overlap if (x[0], x[1]) == (start, stop)]
        same_label = [x for x in overlap if x[2] == label]
        if same_span:
            counts["label"] += 1
            matched_extra.add(same_span[0])
        elif same_label:
            counts["boundary"] += 1
            matched_extra.add(same_label[0])
        elif overlap:
            counts["boundary_and_label"] += 1
            matched_extra.add(overlap[0])
        else:
            counts["missing"] += 1
    counts["extra"] += len(extra - matched_extra)
    return counts


def prf(gold: int, pred: int, correct: int) -> dict[str, Any]:
    precision = correct / pred if pred else 0.0
    recall = correct / gold if gold else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"entity_gold": gold, "entity_pred": pred, "entity_correct": correct,
            "entity_precision": precision, "entity_recall": recall, "entity_f1": f1}


def compare(args: argparse.Namespace) -> int:
    manifest = json.loads(args.manifest_json.read_text(encoding="utf-8"))
    rows = {row["id"]: row for row in load_jsonl(args.input_jsonl)}
    predictions = {row["id"]: row for row in load_jsonl(args.evaluator_predictions)}
    backend = {row["id"]: row for row in load_jsonl(args.backend_output)}
    reference = {row["id"]: row for row in load_jsonl(args.reference_output)} if args.reference_output else None

    totals: Counter[str] = Counter()
    gold_n = evaluator_n = backend_n = evaluator_correct = backend_correct = 0
    mismatches: list[dict[str, Any]] = []
    missing_docs: list[str] = []
    matching = 0

    for group in manifest["groups"]:
        expected: set[Span] = set()
        gold: set[Span] = set()
        for member in group["members"]:
            row = rows[member["id"]]
            pred = predictions[member["id"]]
            if len(pred["pred_labels"]) != len(row["tokens"]):
                raise ValueError(f"{member['id']}: prediction/token length mismatch")
            if reference is None:
                expected |= token_spans_to_char_spans(labels_to_entities(pred["pred_labels"]), row, member["offset"])
            gold |= gold_char_spans(row, member["offset"])
        if reference is not None:
            expected = backend_char_spans(reference[group["id"]])
        if group["id"] not in backend:
            missing_docs.append(group["id"])
            actual: set[Span] = set()
        else:
            actual = backend_char_spans(backend[group["id"]])

        gold_n += len(gold)
        evaluator_n += len(expected)
        backend_n += len(actual)
        evaluator_correct += len(expected & gold)
        backend_correct += len(actual & gold)

        if expected == actual:
            matching += 1
            continue
        counts = classify(expected, actual)
        totals.update(counts)
        mismatches.append({
            "id": group["id"],
            "chars": group["chars"],
            "categories": dict(counts),
            "evaluator_only": sorted(expected - actual),
            "backend_only": sorted(actual - expected),
            "last_expected_offset": max((s[0] for s in expected), default=None),
        })

    summary = {
        "status": "ok" if not mismatches and not missing_docs else "mismatch",
        "reference": "reference-run" if reference is not None else "evaluator",
        "concat_size": manifest["concat_size"],
        "documents": len(manifest["groups"]),
        "matching_documents": matching,
        "mismatched_documents": len(mismatches),
        "documents_missing_from_backend": len(missing_docs),
        "mismatch_categories": dict(totals),
        "reference_metrics": prf(gold_n, evaluator_n, evaluator_correct),
        "backend_metrics": prf(gold_n, backend_n, backend_correct),
    }
    write_json(args.summary_json, summary)
    write_jsonl(args.mismatches_jsonl, mismatches)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if summary["status"] == "ok" else 1


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)

    exp = sub.add_parser("export-input", help="Write backend input JSONL and a group manifest.")
    exp.add_argument("--input-jsonl", type=Path, required=True)
    exp.add_argument("--output-jsonl", type=Path, required=True)
    exp.add_argument("--manifest-json", type=Path, required=True)
    exp.add_argument("--concat-size", type=int, default=1)
    exp.set_defaults(func=export_input)

    ref = sub.add_parser("reference-run", help="Run the verified HF pipeline on backend input.")
    ref.add_argument("--model-dir", type=Path, required=True, help="Downloaded model directory containing pipeline.py")
    ref.add_argument("--backend-input", type=Path, required=True)
    ref.add_argument("--output-jsonl", type=Path, required=True)
    ref.set_defaults(func=reference_run)

    cmp_ = sub.add_parser("compare", help="Compare backend entities with evaluator predictions.")
    cmp_.add_argument("--input-jsonl", type=Path, required=True)
    cmp_.add_argument("--manifest-json", type=Path, required=True)
    cmp_.add_argument("--evaluator-predictions", type=Path, required=True)
    cmp_.add_argument("--backend-output", type=Path, required=True)
    cmp_.add_argument("--reference-output", type=Path, default=None, help="reference-run output; default: evaluator predictions")
    cmp_.add_argument("--summary-json", type=Path, required=True)
    cmp_.add_argument("--mismatches-jsonl", type=Path, required=True)
    cmp_.set_defaults(func=compare)

    args = parser.parse_args(argv)
    if getattr(args, "concat_size", 1) < 1:
        parser.error("--concat-size must be >= 1")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
