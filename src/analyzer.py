from .video_info import get_video_id, get_video_title, extract_title_from_url
from .transcript import get_transcript
from pytube import YouTube
import streamlit as st

def analyze_video(url):
    video_id = get_video_id(url)
    if not video_id:
        return None, None, None, None

    try:
        # Try getting video info using pytube
        yt = YouTube(url)
        title = yt.title
        duration = yt.length
    except Exception as e:
        st.warning(f"No se pudo obtener el titulo del Video. Usando método alternativo.")
        # Fallback: Extract title from URL and use default duration
        title = extract_title_from_url(url) or f"Video {video_id}"
        duration = 0  # Default duration

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
