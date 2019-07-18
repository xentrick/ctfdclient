#!/usr/bin/env python

from pprint import pprint
from ctfdclient import CTFd
from urllib.parse import urljoin


ctfd = CTFd("https://demo.ctfd.io", "admin", "admin", debug=True)
score = ctfd.scoreboard.update()
print("====================================================================")
pprint(ctfd.scoreboard)
print("====================================================================")
pprint(ctfd.scoreboard.__dict__)

for team in ctfd.scoreboard:
    print("====================================================================")
    print(team.name)
    print(team.score)
    print(team.members)
    print(ctfd.scoreboard[team.name])
    print("====================================================================")

ctfd.scoreboard._reset()
print(ctfd.scoreboard.__dict__)

print(ctfd.scoreboard["Art117"])


for t in ctfd.scoreboard:
    for p in t.members:
        print("====================================================================")
        pprint(p.__dict__)
        print("====================================================================")
