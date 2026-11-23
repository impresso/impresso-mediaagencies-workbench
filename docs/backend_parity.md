# Corpus Backend Parity

Corpus processing does not use the Hugging Face pipeline that the release checks verify. It uses the `impresso-inference` mediasources runner, which reimplements tokenization, windowing, the forward pass, and Viterbi decoding for GPU throughput. The backend parity check verifies that this runner reproduces the evaluated model before it touches the collection.

The check compares character-offset entities, not token labels, so it works for any backend that reads Impresso JSONL (`id`, `ft`, `d`) and writes `{"id", "entities": [{"label", "offset": [start, stop]}]}`.

Two inputs are used:

| Input | Built from | Reference | What it catches |
|---|---|---|---|
| `input-c1.jsonl` | the 490 test documents as they are | evaluator decoded predictions | tokenization, decoding, label, and numeric differences |
| `input-c8.jsonl` | 8 test documents joined per synthetic article (62 documents, up to ~46k characters) | the verified HF pipeline run on the same input | truncation and windowing errors on long articles |

Acceptance criterion for a release run: `status: ok` on both inputs, that is 490/490 and 62/62 matching documents.

## Results for model v2.1.0

| Backend | Precision | c1 | c8 |
|---|---|---|---|
| `impresso-inference` `feat/mediasources-decoupled-pipeline` (`abda62b`), transformers 4.57 | CPU fp32 | 241/490, F1 0.452 | 1/62 |
| `impresso-inference` `feat/mediasources-tokenization-windows` (`8e03697`), transformers 5.9 | CPU fp32 | **490/490**, F1 0.8902 | **62/62** |
| same | GPU bf16 | not yet checked | not yet checked |

## Prepare the Inputs and References (Workbench)

Run these once per model release in the workbench. The examples use the v2.1.0 config.

```bash
make evaluate-test CFG=configs/model-v2.1.0.mk SELECTED_MODEL=hf.d/model-v2.1.0 LABEL_MAP=hf.d/model-v2.1.0/label_map.json EVAL_OUTPUT_DIR=staging.d/v2.1.0-test-eval
```

```bash
make backend-parity-input CFG=configs/model-v2.1.0.mk BACKEND_PARITY_CONCAT_SIZE=1
```

```bash
make backend-parity-input CFG=configs/model-v2.1.0.mk BACKEND_PARITY_CONCAT_SIZE=8
```

```bash
make backend-parity-reference CFG=configs/model-v2.1.0.mk BACKEND_PARITY_CONCAT_SIZE=8
```

`backend-parity-reference` needs the published model downloaded to `hf.d/model-v2.1.0`:

```bash
hf download impresso-project/mmbert-impresso-mediasources-ner --revision v2.1.0 --local-dir hf.d/model-v2.1.0
```

The inputs are written to `staging.d/v2.1.0-backend-parity/`.

## Run the Backend on the GPU (bf16)

The GPU machine needs only the two input files and the cookbook environment.

1. Copy the inputs to the GPU machine:

   ```bash
   scp staging.d/v2.1.0-backend-parity/input-c1.jsonl staging.d/v2.1.0-backend-parity/input-c8.jsonl <gpu-host>:~/backend-parity/
   ```

2. On the GPU machine, set up the cookbook environment from the pinned requirements:

   ```bash
   git clone --recursive -b feat/integrate-impresso-inference https://github.com/impresso/impresso-mediasources-cookbook.git
   cd impresso-mediasources-cookbook
   uv venv && source .venv/bin/activate
   uv pip install -r requirements.txt
   uv pip install --no-cache torch --index-url https://download.pytorch.org/whl/cu124
   ```

   Check that the runner sees transformers 5 and the GPU:

   ```bash
   python -c "import transformers, torch; print(transformers.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
   ```

   The mediasources runner refuses to start with transformers 4.x.

3. Run the backend with the production settings (bf16, production batch size) and, as a control, with fp32. Anachronism filtering must be disabled because the references do not filter by publication year.

   ```bash
   cd ~/backend-parity
   for precision in bf16 fp32; do
     for k in 1 8; do
       python -m impresso_inference.tasks.mediasources.cli.run \
         --input input-c$k.jsonl \
         --output backend-$precision-c$k.jsonl \
         --model-name impresso-project/mmbert-impresso-mediasources-ner \
         --revision v2.1.0 \
         --device cuda \
         --precision $precision \
         --batch-size 256 \
         --no-filter-anachronistic 2>&1 | tee backend-$precision-c$k.log
     done
   done
   ```

   Keep `--batch-size` at the value the cookbook config uses (`BATCH_SIZE_MEDIASOURCES`, 256). Batch composition changes padding, and with reduced precision padding can change results.

4. Copy the four outputs back to the workbench:

   ```bash
   scp '<gpu-host>:~/backend-parity/backend-*-c*.jsonl' staging.d/v2.1.0-backend-parity/
   ```

## Compare (Workbench)

Run the comparison for each precision and input:

```bash
make compare-backend-parity CFG=configs/model-v2.1.0.mk EVAL_OUTPUT_DIR=staging.d/v2.1.0-test-eval BACKEND_PARITY_CONCAT_SIZE=1 BACKEND_PARITY_BACKEND_OUTPUT=staging.d/v2.1.0-backend-parity/backend-bf16-c1.jsonl BACKEND_PARITY_SUMMARY_JSON=staging.d/v2.1.0-backend-parity/summary-bf16-c1.json BACKEND_PARITY_MISMATCHES_JSONL=staging.d/v2.1.0-backend-parity/mismatches-bf16-c1.jsonl
```

```bash
make compare-backend-parity CFG=configs/model-v2.1.0.mk EVAL_OUTPUT_DIR=staging.d/v2.1.0-test-eval BACKEND_PARITY_CONCAT_SIZE=8 BACKEND_PARITY_BACKEND_OUTPUT=staging.d/v2.1.0-backend-parity/backend-bf16-c8.jsonl BACKEND_PARITY_SUMMARY_JSON=staging.d/v2.1.0-backend-parity/summary-bf16-c8.json BACKEND_PARITY_MISMATCHES_JSONL=staging.d/v2.1.0-backend-parity/mismatches-bf16-c8.jsonl
```

Repeat both commands with `fp32` in place of `bf16`. With `BACKEND_PARITY_CONCAT_SIZE=1` the comparison uses the evaluator predictions; with `8` it uses the reference pipeline output. The target exits non-zero when parity fails and prints a summary with `matching_documents`, `mismatch_categories`, and entity metrics for the reference and the backend.

## Interpreting the Result

| GPU fp32 | GPU bf16 | Meaning | Action |
|---|---|---|---|
| ok | ok | The production setting reproduces the model. | Run the collection with bf16. |
| ok | a few mismatches, F1 within about 0.002 of the reference | bf16 flips borderline decisions. | Decide whether to accept and record the measured F1 and mismatch count in the run notes, or run with `DTYPE_MEDIASOURCES=float32`. |
| ok | many mismatches or a clear F1 drop | bf16 is not usable with this model. | Run with `DTYPE_MEDIASOURCES=float32`. |
| mismatch | any | The GPU environment differs from the CPU check (library versions, kernels). | Do not run the collection. Compare `transformers`, `torch`, and `tokenizers` versions with the CPU check and inspect `mismatches-fp32-*.jsonl`. |

Mismatch categories in the summary:

- `boundary`: same label, different span. Often punctuation or B/I decisions.
- `label`: same span, different label.
- `missing` / `extra`: entity found by only one side. Many `missing` entities in `c8` but not in `c1` point to truncation or windowing.

The mismatch files list `evaluator_only` (reference) and `backend_only` spans per document, with character offsets into the backend input text.
