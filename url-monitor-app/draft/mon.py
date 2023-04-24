# 

import csv
import requests

def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "OK"
        else:
            return "Error: {}".format(response.status_code)
    except:
        return "Error"

def check_urls():
    urls = []
    with open('urls.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            urls.append(row[0])

    results = []
    for url in urls:
        result = check_url(url)
        results.append([url, result])
    return results

if __name__ == '__main__':
    results = check_urls()

    print("URL Status Monitor")
    print("{:<40} {}".format("URL", "Status"))
    for result in results:
        print("{:<40} {}".format(result[0], result[1]))
