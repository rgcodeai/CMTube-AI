from pytube import YouTube
from urllib.parse import urlparse, parse_qs
import re

def get_video_id(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.netloc == 'youtu.be':
            return parsed_url.path[1:]
        if parsed_url.netloc in ('www.youtube.com', 'youtube.com'):
            if parsed_url.path == '/watch':
                return parse_qs(parsed_url.query)['v'][0]
            if parsed_url.path[:7] == '/embed/' or parsed_url.path[:3] == '/v/':
                return parsed_url.path.split('/')[2]
    except Exception:
        return None
    return None

def get_video_title(url):
    try:
        return YouTube(url).title
    except Exception:
        return extract_title_from_url(url)

def extract_title_from_url(url):
    """Extract a human-readable title from the YouTube URL."""
    try:
        # Try to get title from URL if it contains a title
        parsed_url = urlparse(url)
        if 'title' in parse_qs(parsed_url.query):
            return parse_qs(parsed_url.query)['title'][0].replace('+', ' ')
        
        # If URL contains video ID, use it as fallback
        video_id = get_video_id(url)
        if video_id:
            return f"Video {video_id}"
            
    except Exception:
        pass
    return "Video sin título"
