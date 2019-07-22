#!/usr/bin/env python3

from pprint import pprint
from ctfdclient import CTFd
from ctfdclient.const import API_PREFIX
from urllib.parse import urljoin

def award():
    return

def getSub():
    subs = ctfd.submissions.update()
    for i in ctfd.submissions:
        print(f"""
        ====================================================================
        ID: {i.id}
        Challenge: {i.challenge}
        ChallengeID: {i.challenge_id}
        User: {i.user}
        Type: {i.type}
        Provided: {i.provided}
        ====================================================================""")
    print("Testing retrieval of submission 1")
    pprint(ctfd.submissions.get(1))

def getPlayers():
    players = ctfd.players.update()
    pprint(players)
    for i in ctfd.players:
        print(f"""
        ====================================================================
        ID: {i.id}
        Name: {i.name}
        Country: {i.country}
        ====================================================================""")
    print("Testing retrieval of teams 1")
    pprint(ctfd.players.get(1))

def getTeams():
    teams = ctfd.teams.update()
    pprint(teams)
    for i in ctfd.teams:
        print(f"""
        ====================================================================
        ID: {i.id}
        Name: {i.name}
        Banned: {i.banned}
        ====================================================================""")
    print("Testing retrieval of teams 1")
    pprint(ctfd.teams.get(1))

def getChalls():
    challs = ctfd.challenges.update()
    for i in ctfd.challenges:
        print(f"""
        ====================================================================
        Category: {i.category}
        ID: {i.id}
        Name: {i.name}
        Script: {i.script}
        Tags: {i.tags}
        Template: {i.template}
        Value: {i.value}
        ====================================================================""")
    print("Testing retrieval of challenge 1")
    pprint(ctfd.challenges.get(1))
    

def getScores():
    score = ctfd.scoreboard.update()

    for i in ctfd.scoreboard:
        print(f"""
        ====================================================================
        Name: {i.name}
        Score: {i.score}
        Members: {i.members}
        ====================================================================""")

    # for team in ctfd.scoreboard:
    #     print("====================================================================")
    #     print(team.name)
    #     print(team.score)
    #     print(team.members)
    #     print(ctfd.scoreboard[team.name])
    #     print("====================================================================")
    # for t in ctfd.scoreboard:
    #     for p in t.members:
    #         print("====================================================================")
    #         pprint(p.__dict__)
    #         print("====================================================================")

#ctfd = CTFd("https://demo.ctfd.io", "admin", "admin", debug=True, demo=True)
ctfd = CTFd("http://178.79.132.144:4000", "autopwn", "topwntheeornottopwnthee", debug=True)

#getScores()
# getChalls()
# getTeams()
# getPlayers()
getSub()

#pprint(ctfd.scoreboard.__dict__)
#pprint(ctfd.challenges.__dict__)
#pprint(ctfd.teams.__dict__)
#pprint(ctfd.players.__dict__)
#pprint(ctfd.submissions.__dict__)

# Test award for submission
teamId = 3
userId = 12
chall = 10
ctfd.submissions.give(teamId, userId, chall)
