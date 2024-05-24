from playerClass import Player
import json

classesfile = open('gameStats.json')
allStats = json.load(classesfile)
allClasses = allStats[0]

def gameStart(print,input,currPlayer:Player):
    localName = currPlayer._name
    localClass = currPlayer.className()
    print(f"hello {localName}, I see you are a {localClass}")
