import gradio as gr
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube

# Function to fetch the video ID using pytube
def get_video_id(video_url):
    try:
        yt = YouTube(video_url)
        return yt.video_id
    except Exception as e:
        return None, f"Error extracting video ID: {e}"

# Function to fetch the transcript
def fetch_transcript(video_url):
    try:
        video_id = get_video_id(video_url)
        if not video_id:
            return "Invalid YouTube URL. Please check and try again."
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = "\n".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return f"Error fetching transcript: {e}"

# Create Gradio interface
def transcript_fetcher(video_url):
    return fetch_transcript(video_url)

interface = gr.Interface(
    fn=transcript_fetcher,
    inputs=gr.Textbox(label="YouTube Video URL"),
    outputs=gr.Textbox(label="Video Transcript", lines=15),
    title="YouTube Transcript Fetcher",
    description="Enter a YouTube video URL to fetch its transcript."
)

if __name__ == "__main__":
    interface.launch()
