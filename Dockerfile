FROM debian:bookworm-20220125

RUN apt-get update

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN apt-get install -y tesseract-ocr tesseract-ocr-deu

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]