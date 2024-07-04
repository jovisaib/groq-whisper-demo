# GROQ Whisper V3 Demo

This project demonstrates how to use the GROQ API to transcribe audio files using Streamlit for the web interface.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/groq-whisper-demo.git
    cd groq-whisper-demo
    ```

2. **Install the required dependencies:**

    ```bash
    pip install streamlit groq
    ```

3. **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Open the application:**

    After running the above command, the application will be accessible at `http://localhost:8501`.

2. **Input your GROQ API token:**

    Enter your GROQ API token in the provided text input field.

3. **Upload an audio file:**

    Use the file uploader to upload an audio file. Supported formats are `.wav`, `.mp3`, and `.m4a`.

4. **Transcribe the audio:**

    Click the "Transcribe Audio" button in the sidebar to start the transcription process. The transcription and latency information will be displayed on the main page.

5. **Play the audio file:**

    Use the audio player in the sidebar to play the uploaded audio file.

## Features

- **Audio Transcription:** Transcribe audio files using the GROQ Whisper V3 model.
- **Real-Time Feedback:** Get immediate feedback on transcription status and latency.
- **Audio Playback:** Play uploaded audio files directly within the application.