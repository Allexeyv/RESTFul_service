import json
import requests


def post(url, headers, body):
    r = requests.post(url, data=json.dumps(body), headers=headers)
    status_code = r.status_code
    if status_code == 401:
        return '401 Unauthorized'
    r = r.json()
    return r, status_code


def put(url, headers, body):
    r = requests.put(url, data=json.dumps(body), headers=headers)
    status_code = r.status_code
    if status_code == 401:
        return '401 Unauthorized'
    r = r.json()
    return r, status_code


def get(url, headers):
    r = requests.get(url, headers=headers)
    status_code = r.status_code
    if status_code == 401:
        return '401 Unauthorized'
    try:
        r = r.json()
    except:
        pass
    return r, status_code
