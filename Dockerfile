FROM python:2.7.17-buster
WORKDIR /parsifal
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD . .
VOLUME ["/parsifal-db"]

EXPOSE 8000
ENV PYTHONUNBUFFERED 1
