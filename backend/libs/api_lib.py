from . import request


def get_token(username='admin', password='1111', base_url='http://localhost:8000'):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json;charset=utf-8'}
    url = f'{base_url}/api-token-auth/'

    body = {'username': username, 'password': password}

    r, status_code = request.post(url, headers, body)
    token = r['token']
    return token, status_code