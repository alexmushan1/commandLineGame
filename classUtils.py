import json
import tkinter as tk
from terminal import TerminalApp


classesfile = open('gameStats.json')
allStats = json.load(classesfile)
allClasses = allStats[0]

class Item:
    def __init__(self,name,hpmod,defence,range):
        self.name = name
        self.hpmod = hpmod
        self.defence = defence
        self.range = range

    def hp_modifier(self):
        return int(self.hpmod)
    def defend(self):
        return int(self.defence)
    def applyEffects(self):
        return int(self.hpmod),int(self.defence)
    def itemInfo(self):
        output = ""
        if self.hpmod>=0:
            output = "|healing item| "
        else:
            output = "|deals damage| "
        if self.defence > 0:
            output += "|blocks damage| "
        output = output + "|range = "+str(self.range) +"|"
        return output

class Player:
    def __init__(self, print,input,_name, _class, _ITEMS :list,_ABILITIES:list,OTHERS):
        self._name = _name
        self._class = _class
        self._ITEMS = _ITEMS
        self._ABILITIES = _ABILITIES
        self.OTHERS = OTHERS
        self.print = print
        self.input = input
        self.hp = 100

    def status(self):
        items =[]
        output = f"name: {self._name}, class: {self.className()}, Items: {self._ITEMS}, Abilities: {self._ABILITIES}, others notes: {self.OTHERS}"
        self.print("---------------------------------------")
        self.print("current player status: ")
        self.print(output)
        return output
    
    def className(self):
        myClass = self._class
        return allClasses[str(myClass)]


