from pathlib import Path

EMBEDDINGS_SAVE_PATH = Path(__file__).resolve().parent.joinpath('data', 'embeddings')
TMP_SAVE_PATH = Path(__file__).resolve().parent.joinpath('data', 'tmp')
CHATGPT_API_KEY_FIELD = 'CHATGPT_API_KEY'
CHATGPT_API_KEY = ""
ENVIRONMENT_FILE = ".env"