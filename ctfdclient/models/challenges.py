#!/usr/bin/env python3

from .base import CTFBase
from .ctf import Challenge
from ..const import CHAL_URI

from pprint import pprint

import logging

log = logging.getLogger(__name__)


class Challenges(CTFBase):
    def update(self):
        log.debug("Retrieving challenges...")
        self._reset()
        for i in self._ctfd.get("challenges")["data"]:
            for x in self.challenges:
                if x.name == i["name"]:
                    x.__init__(i)
                    break
            else:
                self.challenges.append(Challenge(i))
        super(Challenges, self).__init__(self._ctfd, self.challenges)

    def get(self, challId):
        if not isinstance(challId, int):
            raise TypeError("Challenge ID has to be an integer")
        info = self._ctfd.get(CHAL_URI.format(challId))["data"]
        if not info:
            return Exception("Challenge ID does not exist")
        return info

    def __init__(self, ctfd, _data=None):
        self._ctfd = ctfd
        self.challenges = []
        super(Challenges, self).__init__(self._ctfd, _data)

    def __iter__(self):
        for x in self.challenges:
            yield x
