from pathlib import Path
TMP_DIR = Path(__file__).resolve().parent.joinpath('data', 'tmp')
print(type(TMP_DIR))