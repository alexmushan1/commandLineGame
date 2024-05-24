import json
import tkinter as tk
from terminal import TerminalApp


classesfile = open('gameStats.json')
allStats = json.load(classesfile)
allClasses = allStats[0]


class Player:
    def __init__(self, print,input,_name, _class, _ITEMS :list,_ABILITIES:list,OTHERS):
        self._name = _name
        self._class = _class
        self._ITEMS = _ITEMS
        self._ABILITIES = _ABILITIES
        self.OTHERS = OTHERS
        self.print = print
        self.input = input
    def status(self):
        output = f"name: {self._name}, class: {self.className()}, Items: {self._ITEMS}, Abilities: {self._ABILITIES}, others notes: {self.OTHERS}"
        self.print("---------------------------------------")
        self.print("current player status: ")
        self.print(output)
        return output
    
    def className(self):
        myClass = self._class
        return allClasses[str(myClass)]
