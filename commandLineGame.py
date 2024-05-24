from pathlib import Path
import os.path
import ast
import events
import json
from classUtils import Player
from terminal import TerminalApp
import tkinter as tk



classesfile = open('gameStats.json')
allStats = json.load(classesfile)
allClasses = allStats[0]
save1 = 'saveFile1.txt'
save2 = 'saveFile2.txt'
save3 = 'saveFile3.txt'

saveInfo = []
currPlayer =None



def initGame():
    if os.path.exists(saveFilePath):
        saveFile = open(saveFilePath,'r')
        ct =0
        content = saveFile.readlines()
        if len(content) <=1:
            return initNewSave()
        try: 
            for line in content:
                words = line.rstrip("\n").split(":")
                if words[0] ==  "NAME":
                    name = words[1]
                elif words[0] ==  "CLASS":
                    pClass = words[1]
                elif words[0] ==  "ITEMS":
                    items = ast.literal_eval(words[1])
                elif words[0] ==  "ABILITIES":
                    abilities = ast.literal_eval(words[1])
                elif words[0] ==  "OTHERS":
                    others = ast.literal_eval(words[1])
            currPlayer = Player(print,input,name,pClass,items,abilities,others)
        except Exception as e:
            print(f"Player Failed to Load: ERROR: {e}")
            return initNewSave()
    else:
        return initNewSave()
    return currPlayer
    

def initNewSave():
    print("creating new save file...")
    in1 = input("Create new save? [y/n]: ")
    if in1.upper() == "N":
        in2 = input("delete this save? [y/n] ")
        if in2.upper() == 'Y':
            outputFile = open(saveFilePath,'w',encoding="utf-8")
            print("save deleted")
        else:
            print("save file is untouched")
        print("going back...")
        return None
    else:
        playerName = input("what is your playername: ")
        print("classes:(1)Soldier, (2)Thief, (3)Monk, (4)Farmer, (5)Archer, (6)Nomad")
        print("choose your class")
        pClass = int(input("enter the number: "))
        print(pClass)
        while pClass not in [1,2,3,4,5,6]:
            pClass = int(input("must choose a valid number: "))
        temp =[]
        currPlayer = Player(print,input,playerName,pClass,temp,temp,temp)
        print(events.saveGame(currPlayer,saveFilePath))
        return currPlayer


def gameloop():
    currPlayer =initGame()
    print("loading player....")
    currPlayer.status()
    running = True
    while running:
        print("---------------------------------------")
        print("-------------MAIN MENU-----------------")
        print("COMMANDS: (1)restart, (2)save, (3)back, (4)start, (0)quit")
        print("---------------------------------------")
        condition = input()
        if condition in  ['quit','0']:
            running = False
            return running
        elif condition in ['back','3']:
            print("going back to main menu...")
            return True
        elif condition in ['restart','1']:
            check = input("are you sure? [y/n]: ")
            if check.upper() == 'Y':
                currPlayer = initNewSave()
                if currPlayer == None:
                    running = False
                    return True
                else:
                    currPlayer.status()
            else:
                print("going back to menu...")
                print("-----------------------")
        elif condition in ['save','2']:
            print(events.saveGame(currPlayer,saveFilePath))
        elif condition in ['start','4']:
            events.gameStart(print,input,currPlayer,saveFilePath)
    
    print(events.saveGame(currPlayer,saveFilePath))


def on_window_close():
    print("enter <quit> or <0> to close the game")
    tkopen = False
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_window_close)
app = TerminalApp(root)
print = app.print
input = app.custom_input
app.run()

while True:
    #-------------------------menu-------------------------------
    saveChosen = input("choose a save file [1],[2],[3] or [0] to quit  ")
    while saveChosen not in ['1','2','3','0','quit']:
            print("enter a valid option:")
            saveChosen = input()
    if saveChosen == '1':
        saveFilePath = save1
    elif saveChosen == '2':
        saveFilePath = save2
    elif saveChosen == '3':
        saveFilePath = save3
    elif saveChosen =='0' or saveChosen.upper() =='QUIT':
        print("GAME EXITED")
        break

    #------------------------------------------------------------

    status = gameloop()
    if not status:
        print("GAME EXITED")
        break

