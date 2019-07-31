#!/usr/bin/env python3

from .base import CTFBase
from .ctf import Submission
from ..const import SUBMISSION_URI

import json
from pprint import pprint

import logging

log = logging.getLogger(__name__)


class Submissions(CTFBase):
    def update(self):
        log.debug("Retrieving submissions...")
        for i in self._ctfd.get("submissions")["data"]:
            for x in self.submissions:
                if x.id == i["id"]:
                    x.__init__(i)
                    break
            else:
                self.submissions.append(Submission(i))
        super(Submissions, self).__init__(self._ctfd, self.submissions)

    def get(self, ident):
        if not isinstance(ident, int):
            raise TypeError("Submission ID has to be an integer")
        info = self._ctfd.get(SUBMISSION_URI.format(ident))["data"]
        if not info:
            return Exception("Submission ID does not exist")
        return info

    def give(self, userId, teamId, challengeId):
        params = {
            "provided": "MARKED AS SOLVED BY ADMIN",
            "user_id": userId,
            "team_id": teamId,
            "challenge_id": str(challengeId),
            "type": "correct",
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "User-Agent": "autopwn",
            "Accept-Language": "en-US,en;q=0.5",
            "CSRF-Token": self._ctfd.nonce,
        }
        resp = self._ctfd.post("submissions", data=json.dumps(params), headers=headers)
        pprint(resp)

    def __init__(self, ctfd, _data=None):
        self._ctfd = ctfd
        self.submissions = []
        super(Submissions, self).__init__(self._ctfd, _data)

    def __iter__(self):
        for x in self.submissions:
            yield x
