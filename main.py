from audiorecorder import audiorecorder
import streamlit as st
import time
import whisper

LANGUAGE = 'pt'

MODELOS = ["tiny", "base", "small", "medium"]

def transcrever_audio(filename, modelo):
    holder = st.markdown(f"Transcrevendo áudio - modelo **{modelo}**...")
    model = whisper.load_model(modelo)
    start_time = time.time()
    result = model.transcribe(filename, fp16=False, language=LANGUAGE)
    end_time = time.time()
    transcricao = result["text"]
    st.markdown(f"### Transcrição do áudio - modelo \"{modelo}\":")
    st.code(transcricao)
    elapsed_time = end_time - start_time
    st.info(f"Tempo decorrido: {elapsed_time:.2f} segundos")
    holder.empty()

st.title("Transcritor de áudio")

audio = audiorecorder("Clique para iniciar a gravação", "Gravando... (clique novamente para encerrar)")
if len(audio) > 0:
    filename = "audio.mp3"
    st.audio(audio.tobytes())
    wav_file = open(filename, "wb")
    wav_file.write(audio.tobytes())
    st.success(f"Áudio gravado: {filename}")
    for modelo in MODELOS:
        transcrever_audio(filename, modelo)
    st.info('Script encerrado.')
    