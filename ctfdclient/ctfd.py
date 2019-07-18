#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

from urllib.parse import urlparse, urljoin
import requests as _requests
from pprint import pprint

from .exceptions import APIException, ClientException
from .const import COOKIE_PREFIX, API_PREFIX
from . import models

# Temporary
_requests.packages.urllib3.disable_warnings()


class CTFd:
    def __init__(self, url, user, pw, debug=False):
        log.info("Initializing ctfdclient")

        self._authed = False

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

        # Models
        self.scoreboard = models.Scoreboard(self, None)

        # Session Setup
        self.session = _requests.Session()
        self.session.verify = False

        # Login and get cookie
        self.login()

    """
    Networking
    """

    def _request(self, method, url, headers=None, **kwargs):
        """ Base function to make requests to CTFd REST API """
        log.debug("{} {}".format(method, url))
        return self._check_error(self.session.request(method, url, **kwargs))

    def _api_request(self, method, uri, headers=None, **kwargs):
        """ Base function to make requests to CTFd REST API """
        url = urljoin(self.api, uri)
        log.debug("API Request: {} {}".format(method, url))
        return self._request(method, url, headers, **kwargs).json()

    def _check_error(self, resp):
        log.debug("Status Code: %s", resp.status_code)
        return resp

    def get(self, uri):
        return self._api_request("GET", uri)

    def post(self, uri, **kwargs):
        return self._api_request("POST", uri, **kwargs)

    def delete(self):
        return self._api_request("DELETE", uri, **kwargs)

    def put(self):
        return self._api_request("PUT", uri, **kwargs)

    """
    Utility
    """

    def login(self):
        log.info("Attempting login...")
        resp = self._request("GET", self.domain)
        if not (resp.cookies.get(COOKIE_PREFIX)):
            raise ClientException(
                "Error getting valid session with CTFd. No cookie found"
            )
        self._authed = True
        log.debug(
            "Cookie Received: {}: {}".format(
                COOKIE_PREFIX, resp.cookies.get(COOKIE_PREFIX)
            )
        )

    """
    Properties
    """

    @property
    def authenticated(self):
        """ Returns true if authententication was successful """
        if self.cookie:
            self._authed = True
        else:
            self._authed = False

        return self._authed

    def cookie(self):
        return self.session.cookies.get(COOKIE_PREFIX)

    def version(self):
        """ Returns version of CTFd being queried. """
        return self._version
