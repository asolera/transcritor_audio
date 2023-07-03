import streamlit as st
import pyaudio
import wave
import whisper

LANGUAGE = 'pt'

def record_audio(duration):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1  # Alterado para 1 canal (mono)
    fs = 44100
    filename = "recording.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []

    st.text("Gravando áudio...")
    for _ in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    st.text("Gravação concluída.")

    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b"".join(frames))
    wf.close()

    return filename


def transcrever_audio(filename):
    model = whisper.load_model("small")
    result = model.transcribe(filename, fp16=False, language=LANGUAGE)
    transcricao = result["text"]
    st.header("Transcrição do áudio:")
    st.text(transcricao)

st.title("Transcritor de áudio")

duration = st.slider("Duração da gravação (em segundos)", 1, 10, 3)
if st.button("Gravar"):
    filename = record_audio(duration)
    st.success(f"Áudio gravado: {filename}")
    st.text("Transcrevendo áudio...")
    transcrever_audio(filename)
