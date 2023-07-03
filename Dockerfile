FROM python:3.9-slim-buster

WORKDIR /app

RUN apt update -y && apt install \
  libasound2 \
  libssl-dev \
  libasound-dev \
  libportaudio2 \
  libportaudiocpp0 \
  portaudio19-dev \
	gcc \
	g++ \
  ffmpeg -y

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "--server.port", "8501", "main.py"]
