from youtube_transcript_api import YouTubeTranscriptApi
import os

RAW_PATH = "data/raw"

def fetch_transcript(video_id: str):

    try:

        ytt_api = YouTubeTranscriptApi()

        # get all available transcripts
        transcript_list = ytt_api.list(video_id)

        # choose first available transcript
        transcript = transcript_list.find_transcript(
            [t.language_code for t in transcript_list]
        )

        data = transcript.fetch()

        text = " ".join([t.text for t in data])

        os.makedirs(RAW_PATH, exist_ok=True)

        with open(f"{RAW_PATH}/{video_id}.txt", "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved transcript {video_id}")

        return text

    except Exception as e:

        print(f"Transcript not available for {video_id}")
        print(e)