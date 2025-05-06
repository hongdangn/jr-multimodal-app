import base64
import streamlit as st
from stt_pipe import pipe, generate_kwargs

def speech_to_text(audio_path):
    description = pipe(audio_path, 
                       chunk_length_s=15, 
                       return_timestamps=False, 
                       generate_kwargs=generate_kwargs)

    return description["text"]

# def text_to_speech(input_text):
#     response = client.audio.speech.create(
#         model="tts-1",
#         voice="nova",
#         input=input_text
#     )
#     webm_file_path = "temp_audio_play.mp3"
#     with open(webm_file_path, "wb") as f:
#         response.stream_to_file(webm_file_path)
#     return webm_file_path

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)