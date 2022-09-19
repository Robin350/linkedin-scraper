FROM python:3.8

COPY .   ./

RUN apt-get update \
    && apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config -y \
    && apt-get install ffmpeg libsm6 libxext6  -y \
    python3 \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN pip install awscli

CMD ["python3","-u","main.py"]


