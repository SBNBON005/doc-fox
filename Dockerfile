FROM python:3.6

RUN mkdir /app

COPY . /app

WORKDIR /app

CMD ["python", "rover.py"]