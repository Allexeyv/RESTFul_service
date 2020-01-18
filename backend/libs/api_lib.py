from . import request

class ApiClient():
    """Provides base operations with api
    """
    def __init__(self, base_url='http://localhost:8000/api/'): 
        self.base_url = base_url
        self.token = None

    def make_headers(self):
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json;charset=utf-8'}
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        return headers

    def login(self, login, password):
        url = f'{self.base_url}/token/'
        headers = self.make_headers()
        body = {'username': login, 'password': password}
        response, status_code = request.post(url, headers, body)
        try:
            self.token = response['access']
            return status_code, 'You are logged in'
        except:
            return status_code, response

    def get_publications(self):
        url = f'{self.base_url}/publication/'
        headers = self.make_headers()
        response = request.get(url, headers)
        return response

    def get_publication(self, id):
        url = f'{self.base_url}/publication/{id}/'
        headers = self.make_headers()
        response = request.get(url, headers)
        return response

    def post_publication(self, data):
        body = data[0]
        url = f'{self.base_url}/publication/'
        headers = self.make_headers()
        response = request.post(url, headers, body)
        return response

    def update_publication(self, data):
        body = data[0]
        id = body['id']
        url = f'{self.base_url}/publication/{id}/'
        headers = self.make_headers()
        response = request.put(url, headers, body)
        return response
        
    def update_category(self, data):
        body = data[0]
        id = body['id']
        url = f'{self.base_url}/publication/{id}/'
        headers = self.make_headers()
        response = request.put(url, headers, body)
        return response

    def get_categories(self):
        url = f'{self.base_url}/category/'
        headers = self.make_headers()
        response = request.get(url, headers)
        return response

    def get_category(self, id):
        url = f'{self.base_url}/category/{id}/'
        headers = self.make_headers()
        response = request.get(url, headers)
        return response

    def post_category(self, data):
        body = data[0]
        url = f'{self.base_url}/category/'
        headers = self.make_headers()
        response = request.post(url, headers, body)
        return response