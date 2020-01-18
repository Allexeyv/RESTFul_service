from . import request

class ApiClient():
    """Provides base operations with api
    """
    def __init__(self, base_url='http://localhost:8000'): 
        self.base_url = base_url
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json;charset=utf-8'}
        self.token = None

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
        if self.token:
            url = f'{self.base_url}/publication/'
            self.headers['Authorization'] = 'token ' + self.token
            response, status_code = request.get(url, self.headers)
            return status_code, response
        else:
            return 'log in first'

    def get_publication(self, id):
        if self.token:
            url = f'{self.base_url}/publication/{id}/'
            self.headers['Authorization'] = 'token ' + self.token
            response, status_code = request.get(url, self.headers)
            return status_code, response
        else:
            return 'log in first'

    # def update_publication(self, data):
    #     pass

    # def update_category(self, data):
    #     pass

    def get_categories(self):
        if self.token:
            url = f'{self.base_url}/category/'
            self.headers['Authorization'] = 'token ' + self.token
            response, status_code = request.get(url, self.headers)
            return status_code, response
        else:
            return 'log in first'

    def get_category(self, id):
        if self.token:
            url = f'{self.base_url}/category/{id}/'
            self.headers['Authorization'] = 'token ' + self.token
            response, status_code = request.get(url, self.headers)
            return status_code, response
        else:
            return 'log in first'