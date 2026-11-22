include configs/model-v2.1.0.mk

HF_DATASET_COMMIT = 26864265198dc5d68fd26018a134574a99caa249
HF_DATASET_LOCAL_DIR = hf.d/dataset-v2.1.0

DATASET_SOURCE_DIR = $(HF_DATASET_LOCAL_DIR)
TRAIN_JSONL = $(DATASET_SOURCE_DIR)/data/train.jsonl
VALIDATION_JSONL = $(DATASET_SOURCE_DIR)/data/validation.jsonl
TEST_JSONL = $(DATASET_SOURCE_DIR)/data/test.jsonl
LABEL_MAP = $(DATASET_SOURCE_DIR)/label_map.json

MODEL = models.d/newsagency_radiostation_modernbert_v2.1.0-hf-verification
SELECTED_MODEL = $(MODEL)/best
