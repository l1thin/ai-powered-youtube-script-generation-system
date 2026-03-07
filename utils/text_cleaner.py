import re

def clean_transcript(text: str):

    # lowercase
    text = text.lower()

    # remove timestamps if present
    text = re.sub(r"\d+:\d+", "", text)

    # remove brackets
    text = re.sub(r"\[.*?\]", "", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()