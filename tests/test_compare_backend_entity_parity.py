import json
from pathlib import Path

from lib.compare_backend_entity_parity import build_groups, classify, main

LABEL = "org.ent.pressagency.afp"


def make_row(doc_id: str, text: str, tokens: list[str], labels: list[str]) -> dict:
    starts, stops, cursor = [], [], 0
    for token in tokens:
        start = text.index(token, cursor)
        starts.append(start)
        stops.append(start + len(token))
        cursor = start + len(token)
    entities = []
    for index, label in enumerate(labels):
        if label.startswith("B-"):
            entities.append({"label": label[2:], "start": starts[index], "stop": stops[index]})
    return {"id": doc_id, "text": text, "date": "1950-01-01T00:00:00+00:00", "tokens": tokens,
            "token_start_offsets": starts, "token_end_offsets": stops, "entities": entities}


ROWS = [
    make_row("a", "Paris ( AFP ) .", ["Paris", "(", "AFP", ")", "."], ["O", "O", f"B-{LABEL}", "O", "O"]),
    make_row("b", "Bern , AFP meldet", ["Bern", ",", "AFP", "meldet"], ["O", "O", f"B-{LABEL}", "O"]),
]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")


def run(tmp_path: Path, concat_size: int, backend_rows) -> tuple[int, dict]:
    test = tmp_path / "test.jsonl"
    write_jsonl(test, ROWS)
    write_jsonl(tmp_path / "pred.jsonl", [{"id": r["id"], "pred_labels": [
        f"B-{LABEL}" if t == "AFP" else "O" for t in r["tokens"]]} for r in ROWS])
    assert main(["export-input", "--input-jsonl", str(test), "--output-jsonl", str(tmp_path / "in.jsonl"),
                 "--manifest-json", str(tmp_path / "m.json"), "--concat-size", str(concat_size)]) == 0
    inputs = [json.loads(line) for line in (tmp_path / "in.jsonl").read_text().splitlines()]
    write_jsonl(tmp_path / "backend.jsonl", backend_rows(inputs))
    code = main(["compare", "--input-jsonl", str(test), "--manifest-json", str(tmp_path / "m.json"),
                 "--evaluator-predictions", str(tmp_path / "pred.jsonl"),
                 "--backend-output", str(tmp_path / "backend.jsonl"),
                 "--summary-json", str(tmp_path / "s.json"), "--mismatches-jsonl", str(tmp_path / "mm.jsonl")])
    return code, json.loads((tmp_path / "s.json").read_text())


def perfect_backend(inputs: list[dict]) -> list[dict]:
    rows = []
    for doc in inputs:
        text, ents, cursor = doc["ft"], [], 0
        while (index := text.find("AFP", cursor)) >= 0:
            ents.append({"label": LABEL, "offset": [index, index + 3]})
            cursor = index + 3
        rows.append({"id": doc["id"], "entities": ents})
    return rows


def test_perfect_backend_matches_with_and_without_concatenation(tmp_path: Path) -> None:
    for size in (1, 2):
        code, summary = run(tmp_path, size, perfect_backend)
        assert code == 0
        assert summary["status"] == "ok"
        assert summary["backend_metrics"]["entity_f1"] == 1.0


def test_truncating_backend_loses_entities_in_concatenated_documents(tmp_path: Path) -> None:
    def truncating(inputs):
        return [{"id": r["id"], "entities": r["entities"][:1]} for r in perfect_backend(inputs)]

    code, summary = run(tmp_path, 2, truncating)
    assert code == 1
    assert summary["mismatch_categories"] == {"missing": 1, "extra": 0}
    assert summary["backend_metrics"]["entity_recall"] == 0.5


def test_build_groups_records_member_offsets() -> None:
    groups = build_groups(ROWS, 2)
    assert groups[0]["members"] == [{"id": "a", "offset": 0}, {"id": "b", "offset": len(ROWS[0]["text"]) + 2}]


def test_classify_distinguishes_boundary_and_label_errors() -> None:
    expected = {(0, 3, "x"), (10, 15, "y")}
    actual = {(0, 5, "x"), (10, 15, "z")}
    assert classify(expected, actual) == {"boundary": 1, "label": 1, "extra": 0}
