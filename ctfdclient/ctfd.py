#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

from urllib.parse import urlparse, urljoin
import requests as _requests
from bs4 import BeautifulSoup
from pprint import pprint

from .exceptions import APIException, ClientException
from .const import COOKIE_PREFIX, API_PREFIX
from . import models

# Temporary
_requests.packages.urllib3.disable_warnings()


class CTFd:
    def __init__(self, url, user, pw, debug=False):
        log.info("Initializing ctfdclient")

        self.authed = False

        # Debug
        if debug:
            log.setLevel(logging.DEBUG)

        # Verify URL
        self.domain = url
        self.api = urljoin(self.domain, API_PREFIX)
        log.debug("CTFd API: {}".format(self.api))

        self.user = user
        self.pw = pw
        log.debug("Username: {}".format(self.user))
        log.debug("Password: {}".format(self.pw))

        # Session Setup
        self.session = _requests.Session()
        self.session.verify = False

        # Login and get cookie
        self.login()

        # Models
        self.scoreboard = models.Scoreboard(self, None)

    """
    Networking
    """

    def _request(self, method, url, **kwargs):
        """ Base function to make requests to CTFd REST API """
        log.debug("{} {}".format(method, url))
        return self._check_error(self.session.request(method, url, **kwargs))

    def _api_request(self, method, url, **kwargs):
        """ Base function to make requests to CTFd REST API """
        url = urljoin(self.api, url)
        log.debug("API Request: {} {}".format(method, url))
        return self._request(method, url, **kwargs).json()

    def _check_error(self, resp):
        log.debug("Status Code: %s", resp.status_code)
        return resp

    def get(self, uri):
        return self._api_request("GET", uri)

    def post(self, uri, body):
        return self._api_request("POST", uri, data=body)

    def delete(self):
        return self._api_request("DELETE", uri, **kwargs)

    def put(self):
        return self._api_request("PUT", uri, **kwargs)

    """
    Utility
    """

    def login(self):
        log.info("Attempting login...")
        loginParams = {"name": self.user, "password": self.pw, "nonce": self.nonce}
        loginUrl = urljoin(self.domain, "login")
        resp = self._request("POST", loginUrl, data=loginParams, allow_redirects=True)
        for r in resp.history:
            pprint(r.headers)
            if 'Set-Cookie' in r.headers:
                self.authed = True
                log.debug("Cookie Received: {}".format(r.headers['Set-Cookie']))
        if not self.authed:
            raise Exception("Error logging into CTFd")

    @property
    def nonce(self):
        log.info("Retreiving nonce for login.")
        resp = self._request("GET", urljoin(self.domain, "login"))
        soup = BeautifulSoup(resp.text, 'lxml')
        #self._nonce = soup.find('input')
        self._nonce = soup.find(attrs={"name": "nonce"})['value']
        return self._nonce

    """
    Properties
    """

    @property
    def cookie(self):
        return self.session.cookies.get(COOKIE_PREFIX)

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if not isinstance(user, str):
            return TypeError("User can only be set to an ascii string.")
        self._user = user

    @property
    def pw(self):
        return self._pw

    @pw.setter
    def pw(self, string):
        if not isinstance(string, str):
            return TypeError("Password can only be set to an ascii string.")
        self._pw = string

    @property
    def api(self):
        return self._api

    @api.setter
    def api(self, location):
        if not isinstance(location, str):
            return TypeError("API location can only be set to an network location.")
        self._api = location

    @property
    def authed(self):
        return self._authed

    @authed.setter
    def authed(self, value):
        if not isinstance(value, bool):
            return TypeError("Authed value must be a bool.")
        self._authed = value
