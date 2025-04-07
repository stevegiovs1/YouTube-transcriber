import os
import streamlit as st
from pytube import YouTube
from faster_whisper import WhisperModel

st.title("Trascrizione YouTube con Faster Whisper")

video_url = st.text_input("Incolla il link del video YouTube")

if st.button("Trascrivi"):
    try:
        if "youtu.be/" in video_url:
            video_url = video_url.split("?")[0].replace("youtu.be/", "www.youtube.com/watch?v=")

        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_path = audio_stream.download(filename="audio.mp4")

        model = WhisperModel("base", compute_type="int8")

        segments, _ = model.transcribe(audio_path)
        transcript = "".join([segment.text for segment in segments])

        st.success("Trascrizione completata!")
        st.write(transcript)

        os.remove(audio_path)

    except Exception as e:
        st.error(f"Errore: {str(e)}")
