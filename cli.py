#!/usr/bin/env python3

from pprint import pprint
from ctfdclient import CTFd
from ctfdclient.const import API_PREFIX
from urllib.parse import urljoin


#ctfd = CTFd("https://demo.ctfd.io", "admin", "admin", debug=True)
ctfd = CTFd("http://178.79.132.144:4000", "autopwn", "topwntheeornottopwnthee", debug=True)

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

#print(ctfd.scoreboard["Art117"])


for t in ctfd.scoreboard:
    for p in t.members:
        print("====================================================================")
        pprint(p.__dict__)
        print("====================================================================")
