import streamlit as st
from groq import Groq
import time


st.title('GROQ Whisper V3 Demo - jovisaib.com')


user_token = st.text_input("GROQ API token")
audio_file = st.file_uploader("Upload Audio", type=["wav","mp3","m4a"])


if st.sidebar.button("Transcribe Audio"):
    if user_token == "":
        st.sidebar.error("Please, input your GROQ API token.")
    elif audio_file is not None:
        client = Groq(api_key=user_token)
        st.sidebar.success("Transcribing audio...")
        try:
            start_time = time.time()
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3",
                response_format="json",
                temperature=0.0
            )
            end_time = time.time()
            latency_ms = (end_time - start_time) * 1000
            st.sidebar.success("Transcription complete!")
            st.markdown(transcription.text)
            st.text(f"Latency: {latency_ms:.2f} ms")
        except Exception:
            st.sidebar.error("Invalid GROQ token.")
    else:
        st.sidebar.error("Please, upload a valid audio file.")


st.sidebar.header("Play Audio File")
st.sidebar.audio(audio_file)