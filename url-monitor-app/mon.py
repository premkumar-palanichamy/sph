import csv
import os
import time
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    return 'ok'

def check_urls():
    while True:
        with open('urls.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                url = row['url']
                try:
                    response = requests.get(url)
                    status_code = response.status_code
                    if status_code == 200:
                        print(f'{name} is UP')
                    else:
                        print(f'{name} is DOWN')
                except Exception as e:
                    print(f'{name} is DOWN')
                    print(str(e))
        time.sleep(600)

if __name__ == '__main__':
    print(os.getcwd()) # prints the current working directory
    check_urls()
