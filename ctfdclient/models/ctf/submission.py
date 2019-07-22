#!/usr/bin/env python
from datetime import datetime
from dateutil.parser import parse
import socket

from .base import InfoBase

import logging

log = logging.getLogger(__name__)

from pprint import pprint


class Submission:
    def __init__(self, _data=None):

        self._data = _data
        pprint(_data)

        self.challenge = self._data["challenge"]
        self.challenge_id = self._data["challenge_id"]
        self.date = self._data["date"]
        self.id = self._data["id"]
        self.ip = self._data["ip"]
        self.provided = self._data["provided"]
        self.team = self._data["team"]
        self.team_id = self._data["team_id"]
        self.type = self._data["type"]
        # self._members = self._data["members"] if self._data["members"] else None
        self.user = self._data["user"]
        self.user_id = self._data["user_id"]

    @property
    def challenge(self):
        return self._challenge

    @challenge.setter
    def challenge(self, val):
        if not isinstance(val, dict):
            raise TypeError("Challenge must be a dict")
        self._challenge = val

    @property
    def challenge_id(self):
        return self._challenge_id

    @challenge_id.setter
    def challenge_id(self, val):
        if not isinstance(val, int):
            raise TypeError("Challenge ID must be an integer")
        self._challenge_id = val

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, val):
        date = parse(val, yearfirst=True)
        if not isinstance(date, datetime):
            raise TypeError("Date must be of `datetime` format")
        self._date = date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError("ID must be an integer")
        self._id = val

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, val):
        if val is not None:
            try:
                socket.inet_aton(val)
            except socket.error:
                raise TypeError("IP must be an IPv4/IPv6 address")
        self._ip = val

    @property
    def provided(self):
        return self._provided

    @provided.setter
    def provided(self, val):
        if not isinstance(val, (str, type(None))):
            raise TypeError("String must be a string")
        self._provided = val

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, val):
        if not isinstance(val, (int, str, type(None))):
            raise TypeError("Team must be an int")
        self._team = val

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, val):
        if not isinstance(val, (int, type(None))):
            raise TypeError("Team ID must be an intger")
        self._team_id = val

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, val):
        if not isinstance(val, str):
            raise TypeError("Type must be a string")
        self._type = val

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, val):
        if not isinstance(val, (int, str, type(None))):
            raise TypeError("User must be an int")
        self._user = val

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, val):
        if not isinstance(val, int):
            raise TypeError("User ID must be an intger")
        self._user_id = val
