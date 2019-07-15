#!/usr/bin/env python


""" Exception classes.
Includes two main exceptions: :class:`.APIException` for when something goes
wrong on the server side, and :class:`.ClientException` for whne something goes
wrong on the client side. Both of these classes extend :class:`.CTFException`.
"""

from .const import RESPONSE_CODES

class CTFException(Exception):
    """ The base CTFd API Exception that all other exception classes extend. """

class APIException(CTFException):
    """ Indicates exception that involves responses from CTFd API. """

    def __init__(self, http_code, http_response=None):
        """ Initialize an instance of APIException.
        :param http_error: The error type returned by CTFd API.
        :param message: The associated message for the error.
        """
        # Super
        if http_code == 400:
            err_msg = '{}: {}'.format(http_code, http_response)
        else:
            err_msg = '{}: {}'.format(http_code, RESPONSE_CODES[str(http_code)])
        super().__init__(err_msg)
        self.http_code = http_code
        self.message = err_msg

class ClientException(CTFException):
    """ Indicates exception that involves an error on the client side. """

    def __init__(self, message=None, *args):
        if message:
            self.message = message
        else:
            self.message = "FATAL: Contact developer."

        # Call the base class constructor with the parameters it needs
        super(ClientException, self).__init__(self.message)
