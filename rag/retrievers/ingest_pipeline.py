import os
import json
from rag.retrievers.chunker import chunk_text
from rag.vectorstores.qdrant_store import create_vectorstore

PROCESSED = "data/processed"

def ingest_data():

    all_chunks = []

    for file in os.listdir(PROCESSED):

        with open(f"{PROCESSED}/{file}", "r", encoding="utf-8") as f:

            data = json.load(f)

        chunks = chunk_text(data["cleaned_transcript"])

        all_chunks.extend(chunks)

    vectordb = create_vectorstore(all_chunks)

    return vectordb