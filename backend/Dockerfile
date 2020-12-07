# Specify a base image
FROM python:3.7

ENV PYTHONUNBUFFERED 1


RUN mkdir /code
WORKDIR /code
RUN apt-get update 
RUN apt-get install -y gunicorn3
RUN python -m pip install --upgrade pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
RUN chmod -R 777 /code
CMD ["bash", "lanch.sh"]
