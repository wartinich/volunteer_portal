FROM python:3.10.4

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]