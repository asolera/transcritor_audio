FROM python:3.9-slim-buster

WORKDIR /app

RUN apt update -y && apt install ffmpeg -y

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["streamlit", "run", "--server.port", "8080", "main.py"]
