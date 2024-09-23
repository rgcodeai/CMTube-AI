from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try to get manually created transcript first
        manual_transcripts = [t for t in transcript_list if not t.is_generated]
        if manual_transcripts:
            transcript = manual_transcripts[0]
        else:
            # If no manual transcript, get the first auto-generated one
            transcript = next(t for t in transcript_list if t.is_generated)
        
        return transcript.fetch(), transcript.language_code
    except Exception as e:
        print(f"Error al obtener la transcripción: {str(e)}")
        return None, None