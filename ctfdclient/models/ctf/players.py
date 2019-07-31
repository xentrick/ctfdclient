#!/usr/bin/env python

from pprint import pprint


class Player:
    def __init__(self, _data):
        self._data = _data

        self.affiliation = self._data["affiliation"]
        self.bracket = self._data["bracket"]
        self.country = self._data["country"]
        self.id = self._data["id"]
        self.name = self._data["name"]
        self.oauth_id = self._data["oauth_id"]
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
    def country(self):
        return self._country

    @country.setter
    def country(self, val):
        if not isinstance(val, (str, type(None))):
            raise TypeError("Name must be string")
        self._country = val

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, val):
        if not isinstance(val, (str, type(None))):
            raise TypeError("E-mail must be string")
        self._email = val

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
