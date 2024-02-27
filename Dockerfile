# FROM python:3.6
FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

WORKDIR /app
COPY ./requires.txt ./requires.txt

RUN pip install -r requires.txt

COPY . .


ENTRYPOINT [ "python", "main.py" ]