from .video_info import get_video_id, get_video_title
from .transcript import get_transcript
from pytube import YouTube

def analyze_video(url):
    video_id = get_video_id(url)
    if not video_id:
        return None, None, None, None

    try:
        yt = YouTube(url)
        title = yt.title
        duration = yt.length  # Get video duration in seconds
    except Exception as e:
        print(f"Error al obtener información del video: {str(e)}")
        title = f"Video {video_id}"  # Título genérico usando el ID del video
        duration = 0  # Duración desconocida

    transcript, language_code = get_transcript(video_id)

    if not transcript:
        return title, None, None, duration

    # Join transcript text
    full_transcript = " ".join([entry['text'] for entry in transcript])
    
    # Split transcript into chunks of approximately 2000 words
    words = full_transcript.split()
    chunk_size = 2000
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

    return title, chunks, language_code, duration
