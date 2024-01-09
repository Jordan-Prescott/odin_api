import requests
import json
class Requester():

    def __init__(self, base_url, api):

        self.api = api
        self.base_url = base_url
        self.headers = {
            'Authorization': "",
            'Content-Type': 'application/json'
        }
    
    def get(self, endpoint, data=None):
        self._check_and_refresh_token
        response = requests.get(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint, data=None):
        self._check_and_refresh_token
        response = requests.post(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None):
        self._check_and_refresh_token
        response = requests.put(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint, data=None):
        self._check_and_refresh_token
        response = requests.delete(
            url=self.base_url + endpoint,
            headers=self.headers,
            data = json.dumps(data if data is not None else {})
        )
        
        response.raise_for_status()
        return response.json()
    
    def _check_and_refresh_token(self):
        if not self.api.is_token_valid():
            self.api.authenticate()
    