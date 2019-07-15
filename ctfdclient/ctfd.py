#!/usr/bin/env python3

import logging
log = logging.getLogger(__name__)

from urllib.parse import urlparse
import requests

from .exceptions import APIException, ClientException

class Client(object):

    def __init__(self, url, user, pw, debug=False):

        self._authed = False

        # Debug
        if debug:
            log.setLogLevel(log.DEBUG)

        # Verify URL
        log.debug("Verifying CTFd URL: {}".format(url))
        self.url = urlparse(url)
        if self.url.scheme is None or self.url.netloc is None:
            raise APIException("Incorrect CTFd URL.")

        self.user = user
        self.pw = pw
        log.debug("Username: {}".format(self.user))
        log.debug("Password: {}".format(self.pw))

        # Session Setup
        self.session = requests.Session()
        self.session.verify = False

    """
    Networking
    """

    def _request(self, path, method="GET", headers=None, **kwargs):
        """ Base function to make requests to CTFd REST API """
        url = urljoin(self.url, path)
        self.log.debug("Method: %s URL: %s", method, url)
        return self._check_error(self.session.request(method=method, url, **kwargs))

    def _check_error(self, resp):
        self.log.debug("Status Code: %s", resp.status_code)
        self.log.debug("JSON:\n%s", resp.json())
        return resp.json()

    def get(self):
        return

    def post(self):
        return

    def delete(self):
        return

    def put(self):
        return

    """
    Properties
    """

    @property
    def authenticated(self):
        """ Returns true if authententication was successful """
        return self._authed

    def version(self):
        """ Returns version of CTFd being queried. """
        return self._version

