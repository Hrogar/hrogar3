print ("HROGAR 3: Queefs of Change")
import math
import sys
import json
from pprint import pprint

from time import sleep
words = "In the Kangdom of Buttholia, a scourge now grips the land. The Wakandans march accross the Buttholian wheatfields and bring terror and EBOLA to the land. Aided by the Longnoses, the Wakandans have been able to conquer the disputed city of Charlottesvisle, which they have renamed to Section Eight. You are Hrogar, and what you have done in your past does not matter, but if you must know, you are a former prison inmate and town rapist, who was wrongfully imprisoned for being too good at being town rapist. After escaping prison, you have traveled back to your hometown of Charlottesvisle, only to find that it is now Section Eight. The time has Cum for the queefer to awaken."
for char in words:
        sleep(0.00)
        sys.stdout.write(char)
        sys.stdout.flush()
##def racewar(Battle function). Keep monster stats inside battle function so only things to import are monster type and player stats?##

def factiondispo (faction,change):
        if (faction+change) > 2 or (faction+change) < -2:
                faction = faction
        if (faction+change) < 3 or (faction+change) > -2:
                faction = faction + change
        return faction

def loadGame():
    try:
        with open('saveGame.json', 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

loaded = loadGame()

race = loaded["race"] if len(loaded) > 0 else 0
level = loaded["level"] if len(loaded) > 0 else 0
chapter = loaded["chapter"] if len(loaded) > 0 else 0
INT = loaded["intelligence"] if len(loaded) > 0 else 0
STR = loaded["strength"] if len(loaded) > 0 else 0
DNG = loaded["thisValIsNotForDong"] if len(loaded) > 0 else 0
y=1
yes = 1
n = 2
no = 2
wakandandispo = loaded["ebtPoints"] if len(loaded) > 0 else -1
longnosedispo = loaded["cutPoints"] if len(loaded) > 0 else -2
wipipodispo = loaded["uncutPoints"] if len(loaded) > 0 else 1

def playerstats ():
    print ("Name:     Hrogar")
    print ("Race:       Nord")
    print ("Level:        ", level)
    print ("Max Health:   ", 10 * STR + math.floor(DNG/2))
    print ("Intelligence: ", INT)
    print ("Strength:     ", STR)
    print ("DONG:         ", DNG)
playerstats()

def saveGame(chapter = 0):
    gameData = {}
    gameData["level"] = level
    gameData["race"] = race
    gameData["intelligence"] = INT
    gameData["strength"] = STR
    gameData["muhDick"] = DNG
    gameData["chapter"] = chapter
    gameData["ebtPoints"] = wakandandispo
    gameData["cutPoints"] = longnosedispo
    gameData["uncutPoints"] = wipipodispo
    with open('saveGame.json', 'w') as outfile:
        json.dump(gameData, outfile)

#Game Start, to be made function later#

print ( )
race = int(input("Pick your race (Nord=1, Wakandan = 0.6, Longnose = 6000000, Liberal Nord = 0:  "))


print ()
while race is not 1:
    race = int(input('Piss off Shitskin. Pick your race (Nord=1, Wakandan = 0.6, Longnose = 6000000:  '))
if race == 1:
    print ("Oh, so you are a Nord then? The Longnoses and Wakandans wont take kindly to you")
    print ()
AP = 16
print ("Points Left: ", AP)
while INT < 1 or INT > 10:
    INT = int(input("Pick intelligence(0 to 10)"))
AP = AP - INT
print ("Points Left: ", AP)
print ()
playerstats()
if AP < 10:
    while STR < 1 or STR > AP:
        print ("Pick strength (0 to",AP,")")
        STR = int(input())
if AP > 9:
    while STR < 1 or STR > 10:
        STR = int(input("Pick strength(0 to 10)"))
AP = AP - STR
print ("Points Left: ", AP)
print ()
playerstats()
if AP < 10:
    while DNG < 1 or DNG > AP:
        print ("Pick DONG (0 to",AP,")")
        DNG = int(input())
if AP > 9:
    while DNG < 1 or DNG > 10:
        DNG = int(input("Pick DONG(0 to 10)"))
AP = AP - STR
playerstats()
#End startgame function#

saveGame(1)
#if chapter(from config file) == 1 :#
print ()
print ("CHAPTER 1: City Gates")
print (" You find yourself at the ancient gates to Charlottesvisle, expecting to see your old friend Bonermere. You instead find a pair of Wakandans gaurdsmen blocking your path. Your ebonix is rusty, but they appear to be asking for your travel papers.")
answer = 0
while answer > 3 or answer < 1:
    print ("Tyrone the Gaurdsman: Ooga booga, mufugguh Bix Nood?")
    print ("Jayvon the Gaurdsman: DAS RIIIIITE")
    print ("1. You was kangz?")
    print ("2. Fuck off Wakandan")
    print ("3. *Show DONG*")
    answer = int(input())
if answer is 2:
    print ("Tyrone the Gaurdsman: Muh Dick (You are denied intry into Charlottesvisle, you are attacked by the gaurdsmen)")
    #Battle Function Here, 2 Gaurds#
    factiondispo(wakandandispo,-1)
if answer is 1:
    print ("Tyrone the Gaurdsman: Hunnit dolla round clip muh WE pyramids hotep WE baybamomma (He enjoys your comment, and has decided he will let you in to the city, but only if you entertain him by fighting a stray cat first)")
    #Battle Function Here, Stray Cat#
    factiondispo(wakandandispo,1)
if answer is 3:
    if DNG > 8:
        print("(Tyrone is angered, and draws his UNESCO provided lead pipe as a weapon. Jayvon is frightened by the DONG and runs off into the woods)")
        #Battle function here, 1 gaurd#
    if DNG < 9:
            print ("Tyrone the Gaurdsman: Muh Dick (You are denied intry into Charlottesvisle, you are attacked by the gaurdsmen)")
            #Battle Function Here, 2 Gaurds#
            factiondispo(wakandandispo,1)
print ("You make it in to the city, though not unscathed. You must find a doctor to heal your health, and cialis potions to restore your dong. The city before you is nothing like what you remember. The streets are dirty, and even more full of potholes than usual. The potholes had been filled in by constant street shitting from the Wakandans. A man dressed in rags approaches you")
print ("Bonermere: Hrogar, dont tell me you dont recognize your old friend Bonermere")
answer = 0
while answer > 4 or answer < 1:
    print ("1. Its good to see you, Bonermere")
    print ("2. My old friend Bonermere. You were second only to me in town raping")
    print ("3. I am injured, Bonermere, and my dong is depleted. I need medecine")
    print ("4. *Show DONG*")
    answer = int(input())
if answer ==1:
    print ("Bonermere: It has been too long, Chartlottesvisle has become a shit hole. We must get you to a doctor. There is only one left in town, I will take you to him, for a price")
if answer ==2:
        print ("And I would have been first, if it werent for that damned Chris Hansen")
if answer ==3:
        print ("Bonermere: It has been too long, Chartlottesvisle has become a shit hole. We must get you to a doctor. There is only one left in town, I will take you to him, for a price")
if answer ==4:
        if DNG >5:
                print ("Bonermere: I can see that prison has not done anything to dampen your spirits, haha")
        if DNG <6:
                print ("Bonermere: You seem....smaller than I remember")
while answer > 1 or answer < 1:
    print ("1. I must see a doctor soon. I have 70,000 Indian Rupees with me to pay him with. I had to do unspeakable things in prison to get them")
    answer = int(input())
print ("Bonermere: Hrogar, since the Wakandans have invaded, Rupees are no longer accepted as currency in Charlottesvisle. We only are allowed to take out loans from the Longnoses and trade the loans as currency")
print ()
print ("OY VEY! DID SOMEBODY SAY LOANS?")
while answer > 2 or answer < 1:
    print ("1. ......")
    print ("2. Who said that??? Show yourself you nasally voiced fiend!")
             answer = int(input())
print ("Amanda (((Bynes))): It is I! Amanda Bynes of the Longnoses. Its a shame that a Nord such as yourself has come to Charlottesvisle without any loans, here, have 20 of them. No need to thank me just pay me back later with a low interest rate of 6,000,000%")
while answer > 3 or answer < 1:
    print ("1. Fine, I will take your filthy loans")
    print ("2. 20 whole loans? Sign me up!")
    if INT >7:
        print("3. How about 100 loans and I promise to touch myself to Wakandan cave paintings later?")
             answer = int(input())
    print ("4. I will never take your fake banker's money!")     
    print()
    print ("Amanda (((Bynes))): You have to take my loans, Nord")

           
