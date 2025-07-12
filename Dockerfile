FROM python:3.11.6-slim-bullseye

WORKDIR /app

COPY ./src /app/src
COPY entrypoint.sh /app/entrypoint.sh
COPY requirements.txt /app/requirements.txt


RUN chmod +x /app/entrypoint.sh
RUN pip install --upgrade pip

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
