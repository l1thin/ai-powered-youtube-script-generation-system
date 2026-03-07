import os
import json
from utils.text_cleaner import clean_transcript

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

for file in os.listdir(RAW):

    with open(f"{RAW}/{file}", "r", encoding="utf-8") as f:
        data = json.load(f)

    cleaned = clean_transcript(data["transcript"])

    data["cleaned_transcript"] = cleaned

    with open(f"{PROCESSED}/{file}", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

print("Processing complete")