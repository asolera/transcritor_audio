# Define a imagem base
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

RUN sudo apt update -y && sudo apt install ffmpeg -y

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto para o diretório de trabalho
COPY . .

# Define a porta em que a aplicação Streamlit irá rodar
EXPOSE 8501

# Comando para executar a aplicação quando o container for iniciado
CMD ["streamlit", "run", "--server.port", "8501", "main.py"]
