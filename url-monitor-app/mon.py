import csv
import time
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Load the URLs from CSV file
urls = []
with open('urls.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        urls.append(row)

@app.route('/')
def get_summary():
    """Returns a summary of monitoring status in the past hour"""
    summary = []
    current_time = time.time()
    for url in urls:
        name = url['name']
        status = url.get('status', {})
        status_time = status.get('time', 0)
        if current_time - status_time <= 3600:
            summary.append({
                'name': name,
                'status': status.get('code', 0)
            })
    return jsonify(summary)

def check_urls():
    """Checks the status of all URLs every 10 minutes"""
    while True:
        for url in urls:
            try:
                response = requests.head(url['url'])
                status_code = response.status_code
            except:
                status_code = -1
            url['status'] = {
                'code': status_code,
                'time': time.time()
            }
        time.sleep(600)

if __name__ == '__main__':
    # Start the URL checking process in a separate thread
    import threading
    url_thread = threading.Thread(target=check_urls)
    url_thread.start()

    # Start the Flask app
    app.run(host='0.0.0.0')
