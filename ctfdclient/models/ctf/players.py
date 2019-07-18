#!/usr/bin/env python

from pprint import pprint


class Player:
    def __init__(self, _data):
        self._data = _data
        self.validate()

        self.id = self._data["id"]
        self.name = self._data["name"]
        self.oauth_id = self._data["oauth_id"]
        self.score = self._data["score"]

    def validate(self):
        if not isinstance(self._data, dict):
            raise Exception("JSON data is not in dictionary format.")
        if self._data["id"] is None:
            raise Exception("No player ID in data")
        if self._data["name"] is None:
            raise Exception("No team name in data")
        if self._data["score"] is None:
            raise Exception("No score value in data")

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
    def id(self):
        return self._id

    @id.setter
    def id(self, idnum):
        if not isinstance(idnum, int):
            raise Exception("ID must be integer")
        self._id = idnum
