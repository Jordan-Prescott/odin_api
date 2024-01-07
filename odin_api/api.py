import requests
import os
import threading

from odin_api.requester import Requester
from odin_api.methods import *
from odin_api.scripter import Scripter
from odin_api.exceptions import (OAApiAuthenticationFail, 
                                 AOSessionRefreshFail, 
                                 AOFailedToLocateSession)


class Api:
    
    def __init__(self, base_url: str, username: str, password: str, token_expiry: int =23) -> None:
        """ Connection to Odin API, all interactions with the api are here.

        Args:
            base_url (str): Base url of your odin instance api.
            username (str): Username used when logging into odin account.
            password (str): Password used when logging into odin account stored as virtual environment.
            
        Vars: 
            authorised (bool): Boolean value to indicate if api is authorised.
            token (str): Token string returned from odin api.
        """
        
        self.base_url = base_url
        self.username = username
        self.password = os.getenv(password)
        
        self.authorised = False
        self.token = ""
        
        self.requester = Requester(self.base_url)
        
        self.get = get.Get(self.requester)
        self.post = post.Post(self.requester)
        self.put = put.Put(self.requester)
        self.delete = delete.Delete(self.requester)
        
        self.timer_started = False
        self.countdown_seconds = token_expiry * 60 * 60  # 24 hours in seconds
        self.timer_thread = threading.Thread(target=self._start_timer)
        self.timer_thread.start()
        
        self.scripter = Scripter(api=self)
 
 
    def authenticate(self):
        
        try:
            response = self.post.session(self.username, self.password)
            self.token = response["token"]
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


    def _start_timer(self):
        self.timer = threading.Timer(self.countdown_seconds, self._token_expired())
        self.timer.start()
        self.timer.join()
        self._start_timer = True


    def _token_expired(self): 
        if self._start_timer: 
            self.refresh_authorisation()


    def __str__(self) -> str:
        return f"API - url: {self.base_url}, username: {self.username}, password: {self.password}." \
            f"Authenticated: {self.authorised}"
    