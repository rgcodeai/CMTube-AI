from .video_info import get_video_id, get_video_title
from .transcript import get_transcript
from pytube import YouTube

def analyze_video(url):
    video_id = get_video_id(url)
    if not video_id:
        return None, None, None, None

    yt = YouTube(url)
    title = yt.title
    duration = yt.length  # Get video duration in seconds
    transcript, language_code = get_transcript(video_id)

    if not transcript:
        return title, None, None, duration

    # Join transcript text
    full_transcript = " ".join([entry['text'] for entry in transcript])
    
    # Split transcript into chunks of approximately 6500 words
    words = full_transcript.split()
    chunk_size = 6500
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

    return title, chunks, language_code, duration