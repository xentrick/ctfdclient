#!/usr/bin/env python
from datetime import datetime
from dateutil.parser import parse

from .base import InfoBase
from .players import Player


import logging
log = logging.getLogger(__name__)

from pprint import pprint


class Team:

    def __init__(self, _data=None):

        self._data = _data

        self.affiliation = self._data["affiliation"]
        self.banned = self._data["banned"]
        self.bracket = self._data["bracket"]
        self.captain_id = self._data["captain_id"]
        self.country = self._data["country"]
        self.created = self._data["created"]
        self.email = self._data["email"]
        self.hidden = self._data["hidden"]
        self.id = self._data["id"]
        # self._members = self._data["members"] if self._data["members"] else None
        self.name = self._data["name"]
        self.oauth_id = self._data["oauth_id"]
        self.secret = self._data["secret"]
        self.website = self._data["website"]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        self._name = name

    @property
    def bracket(self):
        return self._bracket

    @bracket.setter
    def bracket(self, val):
        # if not isinstance(val, str):
        #     raise TypeError("Bracket must be string")
        self._bracket = val

    @property
    def banned(self):
        return self._banned

    @banned.setter
    def banned(self, val):
        if not isinstance(val, bool):
            raise TypeError("Banned must be a bool")
        self._banned = val

    @property
    def captain_id(self):
        return self._captain_id

    @captain_id.setter
    def captain_id(self, val):
        if not isinstance(val, (int, type(None))):
            raise TypeError("Captain ID must be an integer")
        self._captain_id = val

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, val):
        if not isinstance(val, (str, type(None))):
            raise TypeError("Name must be string")
        self._country = val

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, val):
        date = parse(val, yearfirst=True)
        if not isinstance(date, datetime):
            raise TypeError("Creation date must be of DateTime format")
        self._created = date

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, val):
        if not isinstance(val, (str, type(None))):
            raise TypeError("E-mail must be string")
        self._email = val

    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, val):
        if not isinstance(val, bool):
            raise TypeError("Hidden must be bool")
        self._hidden = val

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        if not isinstance(val, int):
            raise TypeError("ID must be an integer")
        self._id = val

    @property
    def oauth_id(self):
        return self._oauth_id

    @oauth_id.setter
    def oauth_id(self, val):
        # if not isinstance(val, str):
        #     raise TypeError("OAuthID must be string")
        self._oauth_id = val

    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, val):
        # if not isinstance(val, str):
        #     raise TypeError("Secret must be a string")
        self._secret = val

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, val):
        if not isinstance(val, (str, type(None))):
            raise TypeError("Website must be string")
        self._website = val

    @property
    def affiliation(self):
        return self._affiliation

    @affiliation.setter
    def affiliation(self, val):
        if not isinstance(val, (str, type(None))):
            raise TypeError("Affilitation must be string")
        self._affiliation = val

    # @property
    # def members(self, val):
    #     return self._members

    # @members.setter
    # def members(self, val):
    #     if not isinstance(val, list):
    #         raise TypeError("Members must be a list")
    #     self._members = val

    # @property
    # def members(self):
    #     return self._members

    # @members.setter
    # def members(self, members):
    #     if not isinstance(members, list):
    #         raise TypeError("Members must be list of Players")

    #     for member in members:
    #         if not isinstance(member, dict):
    #             raise TypeError("Must be a dictionary to populate player data")
    #         self._members.append(Player(member))
