from pathlib import Path

EMBEDDINGS_SAVE_PATH = Path(__file__).resolve().parent.joinpath('data', 'embeddings')
TMP_SAVE_PATH = Path(__file__).resolve().parent.joinpath('data', 'tmp')
CHATGPT_API_KEY_FIELD = 'CHATGPT_API_KEY'
CHATGPT_API_KEY = "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"
ENVIRONMENT_FILE = ".env"