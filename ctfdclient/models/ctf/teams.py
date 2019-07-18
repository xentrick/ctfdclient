#!/usr/bin/env python

from .base import InfoBase
from .players import Player

import logging

log = logging.getLogger(__name__)

from pprint import pprint


class Team:
    def __init__(self, _data=None):

        print("========================TEAM========================================")
        pprint(_data)
        print("====================================================================")

        self.validate(_data)
        self._data = _data
        self._members = []

        self.name = self._data["name"]
        self.score = self._data["score"] if self._data["score"] else 0
        self.members = self._data["members"]

    def validate(self, json):
        if not isinstance(json, dict):
            raise Exception("JSON data is not in dictionary format.")
        if json["account_type"] != "team":
            raise Exception("Invalid account type")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be string")
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise Exception("Score must be integer")
        self._score = score

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, members):
        if not isinstance(members, list):
            raise Exception("Members must be list of Players")

        for member in members:
            if not isinstance(member, dict):
                raise Exception("Must be a dictionary to populate player data")
            self._members.append(Player(member))
