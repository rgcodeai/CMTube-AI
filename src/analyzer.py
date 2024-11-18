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
        title = f"Video {video_id}"  # Generic title using the video ID
        duration = 0 
 # 
    transcript, language_code = get_transcript(video_id)

    if not transcript:
        return title, None, None, duration

    # Process transcript into chunks with start and end times
    chunks = []
    current_chunk = ""
    chunk_start_time = transcript[0]['start']
    word_count = 0

    for entry in transcript:
        words = entry['text'].split()
        word_count += len(words)
        
        if word_count > 3000:
            chunks.append({
                'text': current_chunk.strip(),
                'start_time': chunk_start_time,
                'end_time': entry['start']
            })
            current_chunk = ""
            chunk_start_time = entry['start']
            word_count = len(words)

        current_chunk += " " + entry['text']

    # Add the last chunk
    if current_chunk:
        chunks.append({
            'text': current_chunk.strip(),
            'start_time': chunk_start_time,
            'end_time': transcript[-1]['start'] + transcript[-1]['duration']
        })

    return title, chunks, language_code, duration
