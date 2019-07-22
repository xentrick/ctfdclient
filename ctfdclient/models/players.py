#!/usr/bin/env python3

from .base import CTFBase
from .ctf import Player
from ..const import PLAYERS_URI

from pprint import pprint

import logging

log = logging.getLogger(__name__)


class Players(CTFBase):
    def update(self):
        log.debug("Retrieving players...")
        for i in self._ctfd.get("users")["data"]:
            for x in self.players:
                if x.name == i["name"]:
                    x.__init__(i)
                    break
            else:
                self.players.append(Player(i))
        super(Players, self).__init__(self._ctfd, self.players)

    def get(self, ident):
        if not isinstance(ident, int):
            raise TypeError("Player ID has to be an integer")
        info = self._ctfd.get(PLAYERS_URI.format(ident))["data"]
        if not info:
            return Exception("Player ID does not exist")
        return info

    def __init__(self, ctfd, _data=None):
        self._ctfd = ctfd
        self.players = []
        super(Players, self).__init__(self._ctfd, _data)

    def __iter__(self):
        for x in self.players:
            yield x
