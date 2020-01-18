from . import request

class ApiClient():
    """Provides base operations with api
    """
    def __init__(self, base_url='http://localhost:8000'): 
        self.base_url = base_url
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json;charset=utf-8'}
        self.token = None

    def check_token_exists(self):
        if not self.token:
            return 'log in first'

    def login(self, login, password):
        url = f'{self.base_url}/api-token-auth/'
        headers = self.headers
        body = {'username': login, 'password': password}
        response, status_code = request.post(url, headers, body)
        try:
            self.token = response['token']
            return status_code, 'You are logged in'
        except:
            return status_code, response

    def get_publications(self):
        self.check_token_exists()
        url = f'{self.base_url}/publication/'
        self.headers['Authorization'] = 'token ' + self.token
        response = request.get(url, self.headers)
        return response

    def get_publication(self, id):
        self.check_token_exists()
        url = f'{self.base_url}/publication/{id}/'
        self.headers['Authorization'] = 'token ' + self.token
        response = request.get(url, self.headers)
        return response

    def post_publication(self, data):
        body = data[0]
        self.check_token_exists()
        url = f'{self.base_url}/publication/'
        self.headers['Authorization'] = 'token ' + self.token
        response = request.post(url, self.headers, body)
        return response

    def update_publication(self, data):
        self.check_token_exists()
        body = data[0]
        id = body['id']
        url = f'{self.base_url}/publication/{id}/'
        self.headers['Authorization'] = 'token ' + self.token
        response = request.put(url, self.headers, body)
        return response
        
    def update_category(self, data):
        self.check_token_exists()
        body = data[0]
        id = body['id']
        url = f'{self.base_url}/publication/{id}/'
        self.headers['Authorization'] = 'token ' + self.token
        response = request.put(url, self.headers, body)
        return response

    def get_categories(self):
        self.check_token_exists()
        url = f'{self.base_url}/category/'
        self.headers['Authorization'] = 'token ' + self.token
        response = request.get(url, self.headers)
        return response

    def get_category(self, id):
        self.check_token_exists()
        url = f'{self.base_url}/category/{id}/'
        self.headers['Authorization'] = 'token ' + self.token
        response = request.get(url, self.headers)
        return response

    def post_category(self, data):
        self.check_token_exists()
        body = data[0]
        url = f'{self.base_url}/category/'
        self.headers['Authorization'] = 'token ' + self.token
        response = request.post(url, self.headers, body)
        return response