FROM python:3.9.10

RUN useradd -ms /bin/bash appuser
WORKDIR /home/appuser

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y && rm -rf /var/lib/apt/lists/*

COPY requirements_fastapi.txt ./requirements.txt
RUN pip install -r requirements.txt

USER appuser
EXPOSE 5000
COPY . .

CMD ["python", "predict_fastapi.py"]