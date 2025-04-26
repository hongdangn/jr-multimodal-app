import os
import base64
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyC-45MSDZKaXsINcdEf3gwx8ozNnypdeLw")
client = genai.GenerativeModel("gemini-2.0-flash")

def get_answer(prompt):
    response = client.generate_content(
        prompt
    )
    
    return response.text

def speech_to_text(audio_path):
    audio_file = genai.upload_file(audio_path)

    response = client.generate_content(
        [
            "Please transcribe the audio file without any explaination, just transcribe it.", 
            audio_file
        ]
    )

    return response.text

def text_to_speech(input_text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=input_text
    )
    webm_file_path = "temp_audio_play.mp3"
    with open(webm_file_path, "wb") as f:
        response.stream_to_file(webm_file_path)
    return webm_file_path

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