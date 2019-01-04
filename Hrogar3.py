print ("HROGAR 3: Queefs of Change")
import math
import sys
import json
from pprint import pprint
random.seed(a=None, version=2)
from time import sleep

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

loans = loaded["sheckels"] if len(loaded) > 0 else 0
race = loaded["race"] if len(loaded) > 0 else 0
level = loaded["level"] if len(loaded) > 0 else 0
chapter = loaded["chapter"] if len(loaded) > 0 else 0
INT = loaded["intelligence"] if len(loaded) > 0 else 0
STR = loaded["strength"] if len(loaded) > 0 else 0
DNG = loaded["thisValIsNotForDong"] if len(loaded) > 0 else 0
hp = loaded["gigaslore"] if len(loaded) > 0 else 0
dong = loaded["currentdongpoints"] if len(loaded) > 0 else 0
y=1
yes = 1
n = 2
no = 2
wakandandispo = loaded["ebtPoints"] if len(loaded) > 0 else -1
longnosedispo = loaded["cutPoints"] if len(loaded) > 0 else -2
wipipodispo = loaded["uncutPoints"] if len(loaded) > 0 else 2

def playerstats ():
    print ("Name:     Hrogar")
    print ("Race:       Nord")
    print ("Loans:       ", loans)
    print ("Level:        ", math.floor(level/10))
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
    gameData["sheckels"] = loans
    gameData["gigaslore"] = hp
    gameData["currentdongpoints"] = dong
    with open('saveGame.json', 'w') as outfile:
        json.dump(gameData, outfile)
def beanman():
        global loans
        global cialis
        global ritalin
        global hp
        global dong
        if wipipodispo == -2:
                print ("Beanman: I dont serve traitors like you")
        if wipipodispo > -2:
                answer = 0
                while answer > 5 or answer < 5:
                    print ("Beanman: Well hello there, you look like you could use some supplies, take a look at these wares")
                    print ()
                    print ("Loans:       ", loans)
                    print ()
                    print ("1. [1000000 Loans] *Buy bulk pack of infinite Cialis*")
                    print ("2. [15 Loans] *Buy Ritalin* Can be used to restore 50 Health)")
                    print ("3. [5 Loans] *Buy Cialis* (Can be used to restore DONG)")
                    print ("4. [3 Loans] *Diddle Communal Goat* (Restores Health and DONG)")
                    print ("5. *Show DONG*(and then leave the shop)")
                    answer = int(input())
                    if answer ==1:
                        print ("Beanman: You trying to get a heart attack? You can afford it anyways")
                    if answer ==2:
                        if loans > 14:
                                ritalin = ritalin + 1
                                loans = loans - 15
                                print ("*You receive a ritalin*")
                                print ()
                        if loans < 15:
                                print ("Beanman: You poor bastard, come back with some loans from the Longnoses")
                                print ()
                    if answer == 3:
                        if loans > 4:
                                cialis = cialis + 1
                                loans = loans - 5
                                print ("*You receive a cialis*")
                                print ()
                        if loans < 5:
                                print ("Beanman: You poor bastard, come back with some loans from the Longnoses")
                                print ()
                    if answer == 4:
                        if loans > 2:
                                hp = health
                                dong = DNG
                                loans = loans - 3
                                print ("*You go to work on that goat, youre a goddamned picasso of goat diddling*")
                                print ()
                        if loans < 5:
                                print ("Beanman: You poor bastard, come back with some loans from the Longnoses")
                                print()
                    if answer == 5:
                        print ("You leave the shop")
                        break
##racewar function not finished##
def racewar(enemy,amount):
        print ("You have been challenged to battle by ", amount, enemy)
        if enemy = "straycat":
                enemyhp=30*amount
                enemystr=5*amount
                enemydng=1*amount
                enemyxp=1*amount
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        answer = 0
        battleoutcome = 0
        while battleoutcome == 0:
            print ("Health:", hp, , "/", health)
            print ("DONG:", dong, , "/", DNG)
            print ("1. Use Shank")
            print ("2. Use Cialis for DONG (",cialis, ") remaining")
            print ("3. Use Ritalin for health (",ritalin, ") remaining")
            print ("4. Use DONG for special attack")
            answer = int(input())
            if answer == 1:
                damage = random.randrange(0,STR+1,1)
                enemyhp=enemyhp-damage
                print ("Shank damage: ", damage)
            if answer ==2:
                    if cialis > 0:
                        dong=dong+5
                        cialis = cialis - 1
                        if dong > DNG:
                                dong = DNG
                        print ("DONG restored to ", dong, "inches")
                    if cialis = 0:
                        print ("You have no cialis")
            if answer ==3:
                    if ritalin > 0:
                        hp=hp+50
                        ritalin = ritalin - 1
                        if hp > health:
                                hp = health
                        print ("health restored to ", hp, "points")
                    if ritalin = 0:
                        print ("You have no ritalin")
            if answer == 4:
                damage = random.randrange(0,(STR+1)*(DNG+1),1)
                enemyhp=enemyhp-damage
                print ("You use your dong for ", damage, "damage")
                
#Chapter 0#
words = "In the Kangdom of Buttholia, a scourge now grips the land. The Wakandans march accross the Buttholian wheatfields and bring terror and EBOLA to the land. Aided by the Longnoses, the Wakandans have been able to conquer the disputed city of Charlottesvisle, which they have renamed to Section Eight. You are Hrogar, and what you have done in your past does not matter, but if you must know, you are a former prison inmate and town rapist, who was wrongfully imprisoned for being too good at being town rapist. After escaping prison, you have traveled back to your hometown of Charlottesvisle, only to find that it is now Section Eight. The time has Cum for the queefer to awaken."
for char in words:
        sleep(0.00)
        sys.stdout.write(char)
        sys.stdout.flush()
##def racewar(Battle function). Keep monster stats inside battle function so only things to import are monster type and player stats?##

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
    INT = int(input("Pick intelligence(1 to 10)"))
AP = AP - INT
print ("Points Left: ", AP)
print ()
playerstats()
if AP < 10:
    while STR < 1 or STR > AP:
        print ("Pick strength (1 to",AP,")")
        STR = int(input())
if AP > 9:
    while STR < 1 or STR > 10:
        STR = int(input("Pick strength(1 to 10)"))
AP = AP - STR
print ("Points Left: ", AP)
print ()
playerstats()
if AP < 10:
    while DNG < 1 or DNG > AP:
        print ("Pick DONG (1 to",AP,")")
        DNG = int(input())
if AP > 9:
    while DNG < 1 or DNG > 10:
        DNG = int(input("Pick DONG(1 to 10)"))
AP = AP - STR
loans = 0
cialis = 0
ritalin = 0
health = 0 * STR + math.floor(DNG/2)
hp = health
dong = DNG
playerstats()
#End Chapter 0#

##saveGame(1)##
#Chapter 1#
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
    print ("Bonermere: It has been too long, Chartlottesvisle has become a shit hole. We must get you to a doctor. There is only one left in town, we should head there and reminisce")
if answer ==2:
        print ("And I would have been first, if it werent for that damned Chris Hansen")
if answer ==3:
        print ("Bonermere: It has been too long, Chartlottesvisle has become a shit hole. We must get you to a doctor. There is only one left in town, I will take you to him, for a price")
if answer ==4:
        if DNG >5:
                print ("Bonermere: I can see that prison has not done anything to dampen your spirits, haha")
        if DNG <6:
                print ("Bonermere: You seem....smaller than I remember")
answer = 0
while answer > 1 or answer < 1:
    print ("1. I must see a doctor soon. I have 70,000 Indian Rupees with me to pay him with. I had to do unspeakable things in prison to get them")
    answer = int(input())
print ("Bonermere: Hrogar, since the Wakandans have invaded, Rupees are no longer accepted as currency in Charlottesvisle. We only are allowed to take out loans from the Longnoses and trade the loans as currency")
print ()
print ("OY VEY! DID SOMEBODY SAY LOANS?")
answer = 0
while answer > 2 or answer < 1:
    print ("1. ......")
    print ("2. Who said that??? Show yourself you nasally voiced fiend!")
    answer = int(input())
print ("Amanda (((Bynes))): It is I! Amanda Bynes of the Longnoses. Its a shame that a Nord such as yourself has come to Charlottesvisle without any loans, here, have 20 of them. No need to thank me just pay me back later with a low interest rate of 6,000,000%")
answer = 0
while answer > 3 or answer < 1:
    print ("1. Fine, I will take your filthy loans")
    print ("2. 20 whole loans? Sign me up!")
    if INT >7:
        print("3. How about 100 loans and I promise to touch myself to Wakandan cave paintings later?")
    print ("4. I will never take your fake banker's money!")     
    answer = int(input())
    print()
    print ("Amanda (((Bynes))): You have to take my loans, Nord")
if answer is 1:
        loans = 20
        print("Loans: ", loans)
if answer is 2:
        loans = 20
        print("Loans: ",loans)
if answer is 3:
        if INT >7:
                loans=  100
                print("Loans: ", loans)
        if INT <8:
            loans = 20
            print ("Nice try, only 20 for you Nord")
            print ("Loans: ", loans)  
answer = 0
if loans == 100:
        print ("Bonermere: 100 whole loans? You will be able to by much, but you are going to get completely diddles when the longnoses decide to collet. He who is the richest in Charlottesvisle is now paradoxically the poorest, because of these damned Longnose loans")
if loans == 20:
        print ("Bonermere: 20 loans? You got off easy, but will still be diddled when the longnoses decide to collet. He who is the richest in Charlottesvisle is now paradoxically the poorest, because of these damned Longnose loans")
answer = 0
while answer > 2 or answer < 1:
    print ("1. I dont know how much more of this my DONG can take. Let us go to doctor to get some cialis")
    print ("2. Clearly there is much work to do here in Charlottesvisle, lets get some meds")
    answer = int(input())
print()
print ("You arrive at the a shack near the center of town. A rusted and siphalitic sign reads BEANMAN:MEDICAL RITALIN AND CIALIS")
print ("As you enter the shop, you are greeted by a portly hispanic making salads and sweating profusely")
beanman()
print ()
print ("Bonermere: let us rest, there will be much to do tomorrow")
print ()
print ("End of Chapter 1")
playerstats()
##End of Chapter 2##
##saveGame(2)##
