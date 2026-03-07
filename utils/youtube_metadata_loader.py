from youtube_transcript_api import YouTubeTranscriptApi
import json
import os

RAW_PATH = "data/raw"

def fetch_video_data(video_id):

    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    text = " ".join([t.text for t in transcript])

    data = {
        "video_id": video_id,
        "transcript": text
    }

    os.makedirs(RAW_PATH, exist_ok=True)

    with open(f"{RAW_PATH}/{video_id}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {video_id}")

    return data