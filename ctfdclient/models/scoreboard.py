# from .. import CTFd
from .base import CTFBase
from ..exceptions import APIException, ClientException
from ..const import API_PATH
from .ctf import Team
from json import dumps

# from urllib.parse import urljoin
from pprint import pprint

import logging

log = logging.getLogger(__name__)


class Scoreboard(CTFBase):
    def update(self):
        log.debug("Retrieving scores...")
        self._reset_teams()
        scores = self._ctfd.get("scoreboard")
        for i in scores["data"]:
            self.teams.append(Team(i))
        super(Scoreboard, self).__init__(self._ctfd, self.teams)

    def __init__(self, ctfd, _data=None):
        self._ctfd = ctfd
        self.teams = []
        super(Scoreboard, self).__init__(self._ctfd, _data)

    def __iter__(self):
        for x in self.teams:
            yield x

    # Reset list of teams for pull
    def _reset_teams(self):
        for i in self.teams:
            self._reset(i.name)
        self._reset("teams")
        self.teams = []
