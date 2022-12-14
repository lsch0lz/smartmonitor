FROM python:3.8
WORKDIR /

COPY pages /pages
COPY src /src
COPY Login.py Login.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt