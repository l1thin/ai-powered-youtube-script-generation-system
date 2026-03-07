import os
from utils.text_cleaner import clean_transcript

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

for file in os.listdir(RAW):

    with open(f"{RAW}/{file}", "r", encoding="utf-8") as f:
        text = f.read()

    cleaned = clean_transcript(text)

    with open(f"{PROCESSED}/{file}", "w", encoding="utf-8") as f:
        f.write(cleaned)

print("All transcripts processed successfully")