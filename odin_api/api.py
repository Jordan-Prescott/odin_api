import requests
import os
import jwt

from jwt.exceptions import ExpiredSignatureError

from odin_api.requester import Requester
from odin_api.methods import *
from odin_api.scripter import Scripter
from odin_api.exceptions import (OAApiAuthenticationFail, 
                                 AOSessionRefreshFail, 
                                 AOFailedToLocateSession)


class Api:
    
    def __init__(self, base_url: str, username: str, password: str) -> None:
        """ Connection to Odin API, all interactions with the api are here.

        Args:
            base_url (str): Base url of your odin instance api.
            username (str): Username used when logging into odin account.
            password (str): Password used when logging into odin account stored as virtual environment.
            
        Vars: 
            authorised (bool): Boolean value to indicate if api is authorised.\
            token (str): Token string returned from odin api.
        """
        
        self.base_url = base_url
        self.username = username
        self.password = os.getenv(password)
        
        self.authorised = False
        self.token = ""
        
        self.requester = Requester(self.base_url, api=self)
        
        self.get = get.Get(self.requester)
        self.post = post.Post(self.requester)
        self.put = put.Put(self.requester)
        self.delete = delete.Delete(self.requester)
        
        self.scripter = Scripter(api=self)
 
 
    def authenticate(self):
        
        try:
            response = self.post.session(self.username, self.password)
            self.token = response["token"]
            self._token_header_data = jwt.get_unverified_header(self.token)

            self.requester.headers["Authorization"] = f"Bearer {self.token}"
            self.authorised = True
            return True
        except requests.exceptions.HTTPError:
            raise OAApiAuthenticationFail()
    
    
    def refresh_authorisation(self):
        
        try:
            response = self.put.session()
            self.token = response["token"]
            self.requester.headers["Authorization"] = f"Bearer {self.token}"
            self.authorised = True
            return True
        except requests.exceptions.HTTPError:
            raise AOSessionRefreshFail()
  
    
    def get_auth_details(self):
        
        try:
            return self.get.session()
        except requests.exceptions.HTTPError:
            raise AOFailedToLocateSession()
        
        
    def is_token_valid(self, token):
        jwt.decode(
            token,
            key='am9yZGFuLnByZXNjb3R0OlByZXNjb3R0MjAyMw==',
            algorithms=['HS256', ]
        )
        return True


    def __str__(self) -> str:
        return f"API - url: {self.base_url}, username: {self.username}, password: {self.password}." \
            f"Authenticated: {self.authorised}"
    