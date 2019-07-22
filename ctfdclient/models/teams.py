#!/usr/bin/env python3

from .base import CTFBase
from .ctf import Team
from ..const import TEAM_URI

from pprint import pprint

import logging

log = logging.getLogger(__name__)


class Teams(CTFBase):
    def update(self):
        log.debug("Retrieving teams...")
        for i in self._ctfd.get("teams")["data"]:
            for x in self.teams:
                if x.name == i["name"]:
                    x.__init__(i)
                    break
            else:
                self.teams.append(Team(i))
        super(Teams, self).__init__(self._ctfd, self.teams)

    def get(self, ident):
        if not isinstance(ident, int):
            raise TypeError("Team ID has to be an integer")
        info = self._ctfd.get(TEAM_URI.format(ident))["data"]
        if not info:
            return Exception("Team ID does not exist")
        return info

    def __init__(self, ctfd, _data=None):
        self._ctfd = ctfd
        self.teams = []
        super(Teams, self).__init__(self._ctfd, _data)

    def __iter__(self):
        for x in self.teams:
            yield x
