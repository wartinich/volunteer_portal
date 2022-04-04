FROM python:3.8

RUN mkdir /app

COPY ./requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

RUN chmod 755 /app/prestart.sh