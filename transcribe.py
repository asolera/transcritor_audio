import whisper

filename = "audio001.mp3"
model_name = "small"

print(f"Carregando modelo [{model_name}]...")
model = whisper.load_model(model_name)
print(f"Transcrevendo arquivo [{filename}]...")
result = model.transcribe(filename, fp16=False, language='pt')
transcricao = result["text"]
print("Transcrição do áudio:")
print(transcricao)