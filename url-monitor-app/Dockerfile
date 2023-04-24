FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

RUN mkdir /templates

COPY check.py .

COPY ./csv/urls.csv .

COPY ./templates/index.html ./templates/

COPY ./csv/url_status.csv .

EXPOSE 8080

CMD ["python", "check.py"]
