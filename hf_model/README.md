---
license: mit
language:
- fr
- de
- lb
pipeline_tag: token-classification
tags:
- impresso
- historical-newspapers
- news-agencies
- radio-stations
- media-sources
---

# mmBERT Impresso Media Sources NER

Fine-tuned token-classification model for media-source mention recognition in historical Impresso newspaper text.

The v2.0.1 model predicts cited source mentions for:

- news agencies, labelled as `org.ent.pressagency.<canonical_id>`
- radio stations, labelled as `org.ent.radiostation.<canonical_id>`

The repository name uses "media sources" because the label space may later grow to cover other cited media-source families.

## Provenance

- Dataset: `impresso-project/impresso-mediaagencies-ner-dataset`, revision `v2.1.0`
- Dataset commit: `26864265198dc5d68fd26018a134574a99caa249`
- Training workbench commit: `64f80644b0477dd0743d06e36c2a66b0d9d17764` (dirty worktree at training start)
- Training config: `configs/model-v2.1.0-hf-verification.mk`
- Model revision: `v2.1.0`
- Base model: `impresso-project/mmbert-multilingual-impresso-continued-mlm`
- Upstream base: `jhu-clsp/mmBERT-base`
- License: MIT

## Training Setup

- Annotation tokenization: `unicode-word-punctuation-v1`
- Subtoken supervision: all subtokens labelled, with B-to-I conversion for continuation subtokens
- Adaptation: top 3 ModernBERT layers unfrozen
- Random seed: 42
- Selected checkpoint: epoch 11 (`best`)

## Model Selection

The four decoders were compared on the validation split using the same epoch 11 checkpoint. The release uses `first_subtoken_viterbi`, which achieved the highest validation exact-match entity F1.

| Decoder | Validation entity F1 |
|---|---:|
| `first_subtoken_viterbi` | 0.9290 |
| `all_subtoken_viterbi` | 0.9247 |
| `all_subtoken` | 0.9026 |
| `first_subtoken` | 0.8995 |

The model configuration records the annotation tokenization, subtoken supervision, and decoding policy. Runtime inference applies the declared tokenization and decoder.

## Evaluation

| Split | Precision | Recall | Exact-match entity F1 | Correct / gold / predicted |
|---|---:|---:|---:|---:|
| Validation | 0.9567 | 0.9029 | 0.9290 | 530 / 587 / 554 |
| Held-out test | 0.9341 | 0.8502 | 0.8902 | 539 / 634 / 577 |

The local custom pipeline reproduced the evaluator's decoded BIO labels on all 490 test documents, with zero mismatches and identical entity and token metrics. Verification of the published artifact is pending.

## Intended Use

Use this model to identify cited news-agency and radio-station source mentions in historical newspaper text. The model is intended for corpus enrichment and assisted curation workflows, not as a general-purpose named-entity recognizer.

The input text should be tokenized with the same annotation-tokenization policy used by the training data. For deployment through the custom pipeline files in this repository, use the model's configured `first_subtoken_viterbi` decoding policy.
