from classUtils import Player
from classUtils import Item
import json


classesfile = open('gameStats.json')
itemsfile = open('items.json')

allStats = json.load(classesfile)
allClasses = allStats[0]
allItems = allStats[1]
itemMenu = json.load(itemsfile)

def gameStart(print,input,currPlayer:Player,saveFilePath):
    localName = currPlayer._name
    localClass = currPlayer.className()
    print(f"hello {localName}, I see you are a {localClass}")
    print("--------------------------------------")
    items = currPlayer._ITEMS
    if (len(items)==0):
        print("You don't have anything with you, I got something for you, do you want it? [y/n]")
        answer = input()
        if answer in ['n','N']:
            answer = input("are you sure about that? [y/n]")
            if answer in ['n','N']:
                print("ok then")
        else:
            firstWeapon(print,input,currPlayer)
            input("do you like it?")
            print("well, it does not matter")
    
    while True:
        print("let's go on advantures shall we?")
        print("--------------------------------------")
        print("OPTIONS: (1)adventure, (2)house, (3)practice, (4)save, (0)back to menu")
        print("--------------------------------------")
        answer = input()
        if answer in ['4']:
            print(saveGame(currPlayer,saveFilePath))
        elif answer in ['1']:
            pass
        elif answer in ['2']:
            pass
        elif answer in ['3']:
            pass
        elif answer in ['0']:
            print("loading menu...")
            break
        else:
            print("try another option")


def firstWeapon(print,input,currPlayer:Player):
    classNUM = currPlayer._class
    weapon = allItems[str(classNUM)]
    print(f"here is a {weapon} for you")
    currPlayer._ITEMS.append(weapon)
    return
            
def initItems(currPlayer:Player,itemName):
    attributes = itemMenu[itemName]
    item = Item(itemName,attributes['hpmod'],attributes['defence'],attributes['range'])
    return item

def saveGame(currPlayer:Player,saveFilePath):
    
    outputFile = open(saveFilePath,'w',encoding="utf-8")
    outputFile.write(f"NAME:{currPlayer._name}\n")
    outputFile.write(f"CLASS:{currPlayer._class}\n")
    outputFile.write(f"ITEMS:{currPlayer._ITEMS}\n")
    outputFile.write(f"ABILITIES:{currPlayer._ABILITIES}\n")
    outputFile.write(f"OTHERS:{currPlayer.OTHERS}\n")
    currPlayer.status()
    outputFile.close()
    return "...............................................game saved"
