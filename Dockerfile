# app/Dockerfile

FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/dikshamagotra123/RecommendationSystem.git .

COPY archive archive/

COPY datasets datasets/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "gui.py", "--server.port=8501", "--server.address=0.0.0.0"]