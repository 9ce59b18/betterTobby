FROM python:alpine3.11 AS builder

WORKDIR /app

COPY requirements.txt ./
COPY main.py ./
COPY templates ./templates

RUN python3 -m pip install -r requirements.txt


EXPOSE 3073

CMD ["python3", "main.py"]
