from .base import CTFBase
from .ctf import Team
# from .. import CTFd
# from ..exceptions import APIException, ClientException
# from urllib.parse import urljoin
# from pprint import pprint

import logging

log = logging.getLogger(__name__)


class Scoreboard(CTFBase):
    def update(self):
        log.debug("Retrieving scores...")
        self._reset()
        for i in self._ctfd.get("scoreboard")["data"]:
            for x in self.scores:
                if x.name == i["name"]:
                    x.__init__(i)
                    break
            else:
                self.scores.append(Team(i))
        super(Scoreboard, self).__init__(self._ctfd, self.scores)

    def __init__(self, ctfd, _data=None):
        self._ctfd = ctfd
        self.scores = []
        super(Scoreboard, self).__init__(self._ctfd, _data)

    def __iter__(self):
        for x in self.scores:
            yield x
