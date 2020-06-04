#!/usr/bin/python3
import requests


URL = "http://158.69.76.135/level0.php"

payload = {"id": "1406", "holdthedoor": "Submit+Query"}

for a in range(1024):
    response = requests.post(URL, data=payload)
    if response.status_code == 200:
        print("{:d} The request has succeeded.".format(a))
    else:
        print("{:d} The request has failed.".format(a))
        break
