import json
import requests


def post(url, headers, body):
    r = requests.post(url, data=json.dumps(body), headers=headers)
    status_code = r.status_code
    r = r.json()
    return r, status_code


def get(url, headers):
    r = requests.get(url, headers=headers)
    status_code = r.status_code
    r = r.json()
    return r, status_code
