import csv
import os
import time
import requests
from flask import Flask, render_template
import schedule

app = Flask(__name__)

@app.route('/')
def health():
    results = []
    with open('url_status.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            results.append(row)
    return render_template('index.html', results=results)

def check_urls():
    results = []
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
                    result = (name, 'UP')
                else:
                    print(f'{name} is DOWN')
                    result = (name, 'DOWN')
            except requests.exceptions.RequestException as e:
                print(f'{name} is DOWN')
                print(str(e))
                result = (name, 'DOWN: ' + str(e))
            results.append(result)
    with open('url_status.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Status'])
        for result in results:
            writer.writerow(result)
    print("URL Status Monitor")
    print("{:<40} {}".format("URL", "Status"))
    for result in results:
        print("{:<40} {}".format(result[0], result[1]))
    # Update the webpage with the latest results
    return results

if __name__ == '__main__':
    # Run check_urls() every 2 minutes
    schedule.every(2).minutes.do(check_urls)
    # Continuously update the webpage with the latest results
    while True:
        results = check_urls()
        app.run(host='0.0.0.0', port=8080, debug=False)
        time.sleep(120)
