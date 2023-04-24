FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY moni.py .

COPY urls.csv .

EXPOSE 8080

CMD ["python", "moni.py"]
