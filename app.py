import streamlit as st
from groq import Groq

client = Groq()

st.title('GROQ Whisper V3 Demo - jovisaib.com')



audio_file = st.file_uploader("Upload Audio", type=["wav","mp3","m4a"])



if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing audio...")
        transcription = "adsasassa do request"
        st.sidebar.success("Transcription complete!")
        st.text(transcription["text"])
    else:
        st.sidebar.error("Please, upload an audio file.")
# from streamlit_mic_recorder import mic_recorder
# audio = mic_recorder(
#     start_prompt="Start recording",
#     stop_prompt="Stop recording",
#     just_once=False,
#     use_container_width=False,
#     callback=None,
#     args=(),
#     kwargs={},
#     key=None
# )