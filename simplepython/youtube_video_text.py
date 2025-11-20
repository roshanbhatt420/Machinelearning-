from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(url: str) -> str:
    """
    Extracts video ID from any YouTube URL.
    """
    parsed_url = urlparse(url)

    # Case 1: https://youtu.be/<id>
    if parsed_url.netloc in ["youtu.be"]:
        return parsed_url.path[1:]

    # Case 2: https://www.youtube.com/watch?v=<id>
    if parsed_url.path == "/watch":
        return parse_qs(parsed_url.query)["v"][0]

    # Case 3: Embedded links or other formats
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]

    raise ValueError("Could not extract video ID from URL")


def fetch_youtube_transcript(url: str) -> str:
    """
    Converts URL → video ID → transcript text.
    Returns full transcript as one string.
    """
    video_id = get_video_id(url)
    ytt_api=YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)

    for snippet in fetched_transcript:
      return snippet.text


# Example use
youtube_url = input("Enter the video url")
text = fetch_youtube_transcript(youtube_url)
print(text)
