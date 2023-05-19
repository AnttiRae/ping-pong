FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=8000
ENV PONG_FILE=pong.log
ENV LOG_FILE=app.log
ENV PONG_SERVER_URL=http://localhost:8080/pingpong

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
