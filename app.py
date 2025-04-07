import os
import streamlit as st
from pytube import YouTube
import whisper

st.set_page_config(page_title="Trascrizione YouTube", layout="centered")

st.title("Trascrivi l’audio di un video YouTube")
st.markdown("Incolla il link di un video e ottieni la trascrizione automatica dell’audio.")

video_url = st.text_input("Inserisci il link del video YouTube")

if st.button("Trascrivi"):
    if not video_url:
        st.warning("Per favore, inserisci un link.")
    else:
        try:
            st.info("Scarico l'audio dal video...")
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_path = audio_stream.download(filename="temp_audio.mp4")

            st.info("Avvio la trascrizione...")
            model = whisper.load_model("base")  # Puoi usare anche "small" o "medium"
            result = model.transcribe(audio_path)

            st.success("Trascrizione completata!")
            st.subheader("Testo trascritto:")
            st.write(result["text"])

            os.remove(audio_path)

        except Exception as e:
            st.error(f"Errore: {str(e)}")
