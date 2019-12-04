FROM python:2.7.17-buster
WORKDIR /parsifal
ADD ./requirements.txt .
RUN pip install -r requirements.txt
ADD . .
VOLUME ["/parsifal-db"]

EXPOSE 8000
ENV PYTHONUNBUFFERED 1
#RUN ["python", "manage.py", "makemigrations"]
#RUN ["python", "manage.py", "migrate"]
#ENTRYPOINT ["/bin/bash"]
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8080"]
