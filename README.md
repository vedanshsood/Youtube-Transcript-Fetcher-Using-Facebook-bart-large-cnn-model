# YouTube Transcript Fetcher

YouTube Transcript Fetcher is a Python-based web application that extracts and displays the transcript of a YouTube video by simply entering its URL. It uses `Gradio` for the user interface, `pytube` to extract the video ID, and `youtube-transcript-api` to fetch the transcript.

---

## Features

- Extracts transcripts from YouTube videos with captions.
- User-friendly web interface powered by Gradio.
- Handles invalid URLs and videos without transcripts gracefully.

---

## Prerequisites

Before using the project, ensure you have the following:

- Python 3.7 or higher
- Pip (Python package manager)

---

## Installation

1. Clone the repository or save the script locally.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Save the script as `youtube_transcript_fetcher.py`.

---

## Usage

1. Run the Python script:
   ```bash
   python youtube_transcript_fetcher.py
   ```

2. Open the Gradio interface in your browser (usually at `http://127.0.0.1:7860`).

3. Enter a YouTube video URL in the input field.

4. View the transcript in the output field if available.

---

## Project Files

- `youtube_transcript_fetcher.py`: Main script for the application.
- `requirements.txt`: List of required Python libraries.

---

## Code Overview

### Main Functions

- **`get_video_id(video_url)`**:
  Extracts the video ID from a given YouTube URL using `pytube`.

- **`fetch_transcript(video_url)`**:
  Fetches the transcript of a video using `youtube-transcript-api`. Handles errors like invalid URLs or missing captions.

- **Gradio Interface**:
  A simple web interface allows users to input a video URL and fetch the transcript.

---

## Libraries Used

- **Gradio**: For building the web-based user interface.
- **pytube**: To extract video metadata from YouTube URLs.
- **youtube-transcript-api**: To fetch the transcript from YouTube's caption system.

---

## Known Limitations

- Only works with videos that have captions enabled.
- Does not support auto-generated captions yet.

---

## License

This project is licensed under the MIT License.

---

## Author

Vedansh Sood  
