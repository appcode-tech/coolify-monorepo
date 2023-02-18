FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app

RUN pip install flask

COPY app.py .

CMD ["python", "app.py"]