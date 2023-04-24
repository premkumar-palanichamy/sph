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
                    response = requests.get(url, timeout=10)
                    status_code = response.status_code
                    if status_code == 200:
                        print(f'{name} is UP')
                    else:
                        print(f'{name} is DOWN')
                #except Exception as e:
                except requests.exceptions.RequestException as e:
                    print(f'{name} is DOWN')
                    print(str(e))
        time.sleep(600)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)   
    # results = check_urls()

    # print("URL Status Monitor")
    # print("{:<40} {}".format("URL", "Status"))
    # for result in results:
    #     print("{:<40} {}".format(result[0], result[1]))
    #print(os.getcwd()) # prints the current working directory
    #check_urls()
    #app.run(host='0.0.0.0', port=8080, debug=False)
    #app.run(host='0.0.0.0')