#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

from urllib.parse import urlparse, urljoin
import requests as _requests
from pprint import pprint

from .exceptions import APIException, ClientException
from .const import COOKIE_PREFIX

# Temporary
_requests.packages.urllib3.disable_warnings()


class Client(object):
    def __init__(self, url, user, pw, debug=False):
        log.info("Initializing ctfdclient")

        self._authed = False

        # Debug
        if debug:
            log.setLevel(logging.DEBUG)

        # Verify URL
        log.debug("CTFd Location: {}".format(url))
        self.url = url

        self.user = user
        self.pw = pw
        log.debug("Username: {}".format(self.user))
        log.debug("Password: {}".format(self.pw))

        # Session Setup
        self.session = _requests.Session()
        self.session.verify = False

        # Login and get cookie
        self.login()

    """
    Networking
    """

    def _request(self, uri="/", method="GET", headers=None, **kwargs):
        """ Base function to make requests to CTFd REST API """
        url = urljoin(self.url, uri)
        log.debug("{} {}".format(method, url))
        # params = **kwargs
        return self._check_error(self.session.request(method, url, **kwargs))

    def _check_error(self, resp):
        log.debug("Status Code: %s", resp.status_code)
        return resp

    def get(self, uri):
        return self._request(uri, method="GET")

    def post(self, uri, **kwargs):
        return self._request(uri, method="POST", **kwargs)

    def delete(self):
        return self._request(uri, method="DELETE", **kwargs)

    def put(self):
        return self._request(uri, method="PUT", **kwargs)

    """
    Utility
    """

    def login(self):
        log.info("Attempting login...")
        resp = self.get(self.url)
        if not (resp.cookies.get(COOKIE_PREFIX)):
            raise ClientException("Error getting valid session with CTFd. No cookie found")
        self._authed = True
        log.debug("Cookie Received: {}: {}".format(COOKIE_PREFIX, resp.cookies.get(COOKIE_PREFIX)))

    """
    Properties
    """

    @property
    def authenticated(self):
        """ Returns true if authententication was successful """
        return self._authed

    def cookie(self):
        return self.session.cookies.get(COOKIE_PREFIX)

    def version(self):
        """ Returns version of CTFd being queried. """
        return self._version
