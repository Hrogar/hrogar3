print ("HROGAR 3: Queefs of Change")
print ("By AssMaster Studios")
import math
import sys
import json
from pprint import pprint
import random
random.seed(a=None, version=2)
from time import sleep

def loadGame():
    try:
        with open('saveGame.json', 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

loaded = loadGame()

health = loaded["livin"] if len(loaded) > 0 else 0
exp = loaded["muhnigga"] if len(loaded) > 0 else 0
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
    print ("Level:        ", level)
    print ("Max Health:   ", health)
    print ("Intelligence: ", INT)
    print ("Strength:     ", STR)
    print ("DONG:         ", DNG)

def saveGame(chapter = 0):
    gameData = {}
    gameData["livin"] = health
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
    gameData["muhnigga"] = exp
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
def racewar(enemy,amount):
        if enemy == 1:
                print ("You have been challenged to battle by ", amount, "straycat")
                #straycat#
                enemyhp=25*amount
                enemystr=5
                enemydng=1*amount
                enemyxp=1*amount
        if enemy == 2:
                print ("You have been challenged to battle by ", amount, "Wakandan Gaurdsmen")
                #Wakandan Gaurdsman#
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 3:
                print ("You have been challenged to battle by ", amount, "Beanman")
                #Beanman#
                enemyhp=85*amount
                enemystr=9
                enemydng=3*amount
                enemyxp=9*amount
        if enemy == 4:
                print ("You have been challenged to battle by ", amount, "crocodile")
                #Crocodile#
                enemyhp=35*amount
                enemystr=11
                enemydng=1*amount
                enemyxp=3*amount
        if enemy == 5:
                print ("You have been challenged to battle by ", amount, "Double Wakandan")
                #Double Wakandan#
                enemyhp=60*amount
                enemystr=12
                enemydng=1*amount
                enemyxp=4*amount
        if enemy == 6:
                print ("You have been challenged to battle by ", amount, "Nigerius Liberius")
                #Nigerius Liberius#
                enemyhp=100*amount
                enemystr=15
                enemydng=1*amount
                enemyxp=9*amount
        if enemy == 7:
                print ("You have been challenged to battle by ", amount, "Beta Orbiters")
                #Beta Orbiter#
                enemyhp=2*amount
                enemystr=1
                enemydng=1*amount
                enemyxp=1
        if enemy == 8:
                print ("You have been challenged to battle by ", amount, "Lauren Southern")
                #Ethota#
                enemyhp=120*amount
                enemystr=18
                enemydng=1*amount
                enemyxp=9
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global DNG
        global exp
        global loans
        answer = 0
        battleoutcome = 0
        while battleoutcome == 0:
            print ()
            print ("Health:", hp, "/", health)
            print ("DONG:", dong, "/", DNG)
            print ("1. Use Shank")
            print ("2. Use Cialis for DONG (",cialis, ") remaining")
            print ("3. Use Ritalin for health (",ritalin, ") remaining")
            print ("4. Use DONG for special attack")
            answer = int(input())
            if answer == 1:
                damage = random.randrange(0,STR+1,1)
                enemyhp=enemyhp-damage
                print ("You shank the enemy for ", damage, " damage")
            if answer ==2:
                    if cialis > 0:
                        dong=dong+5
                        cialis = cialis - 1
                        if dong > DNG:
                                dong = DNG
                        print ("DONG restored to ", dong, "inches")
                    if cialis == 0:
                        print ("You have no cialis")
            if answer ==3:
                    if ritalin > 0:
                        hp=hp+50
                        ritalin = ritalin - 1
                        if hp > health:
                                hp = health
                        print ("health restored to ", hp, "points")
                    if ritalin == 0:
                        print ("You have no ritalin")
            if answer == 4:
                    if dong >0:
                        damage = random.randrange(5,STR*5+1,1)
                        enemyhp=enemyhp-damage
                        print ("You use your dong for ", damage, "damage")
                        dong = dong - 1
                    if dong < 1:
                            print ("Your DONG is not working")
            if enemyhp < 1:
                print ("You have defeated the enemy")
                print ("Exp Gained: ", enemyxp)
                exp = exp + enemyxp
                coinss = random.randrange(0,enemyxp*2,1)
                print ("You have gained ", coinss, " loans")
                loans = loans + coinss
                while exp > (15-INT):
                        print ("You have leveled up")
                        level = level + 1
                        exp = exp - (15-INT)
                        strboost = random.randrange(1,3,1)
                        hpboost = random.randrange(1,5,1)
                        dngboost = math.floor(random.randrange(0,6,1)/5)
                        print ("DONG: +", dngboost)
                        print ("Strength: +",strboost)
                        print ("Additional Health: +", hpboost)
                        STR = STR + strboost
                        health = health + hpboost
                        DNG = DNG + dngboost
                        playerstats()
                break
            turns= amount
            while turns > 0:
                dongchance = random.randrange(1,6,1)
                if dongchance < 5:
                    damage = random.randrange(0,enemystr+1,1)
                    hp=hp-damage
                    print ("You are attacked for ", damage, "damage")
                if dongchance > 4:
                    damage = random.randrange(3,enemystr*2,1)
                    hp=hp-damage
                    print ("You are attacked with a DONG for ", damage, "damage")
                turns=turns-1
            print ("Enemy total Health: ", enemyhp)
            if hp < 1:
                    print ("You have died, the enemy diddles your corpse")
                    print ("GAME OVER")
                    youdednigga=input()
                    while health > 0:
                            print ("Game Over Loser")
def ch3roaming():
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global DNG
        global exp
        global loans
        global wipipodispo
        answer = 0
        while answer > 4 or answer < 1:
            print ("What to do?")
            print ("1. Visit Beanman")
            print ("2. Visit tavern")
            print ("3. *Show DONG* to passerby")
            print ("4. *Visit Ethota")
            answer = int(input())
            if answer == 1:
                    beanman()
                    answer = 0
            if answer == 2:
                    print ("You visit your favorite tavern, the DONG Forrest Tavern, and take a seat. You notice some Wakandan gaurdsmen are being rowdy and chimping out at the bartender")
                    answer = 0
                    while answer > 3 or answer < 1:
                        print ("What to do?")
                        print ("1. [2 Loans] Order drink")
                        print ("2. Confront Wakandans")
                        print ("3. *Show DONG* and leave")
                        answer = int(input())
                    if answer == 1:
                        if loans >1:
                            loans = loans - 2
                            dong = DNG
                            hp = health
                            print ("Gritty, but refreshing. You forget where you are and leave the tavern")
                            answer = 0
                        if loans < 2:
                            print ("You are too poor, you are kicked out of the tavern")
                            answer = 0
                    if answer == 2:
                        print ("Wakandan: Hunnit EBT (State your business here, Nord)")
                        answer = 0
                        while answer > 3 or answer < 1:
                            print ("1. Fight me, spearchuckers")
                            print ("2. Leave bar")
                            print ("3. *Show DONG*")
                            answer = int(input())
                            if answer ==1:
                                racewar (2,5)
                                print(" The Wakandans yell something about kangz and leave the bar. You get a free drink from the bartender, which you finish in peace and leave")
                                hp = health
                                dong = DNG
                                wipipodispo = 3
                            if answer == 2:
                                print ("You leave the bar and are mugged on the way out for all of your loans")
                                loans = 0
                            if answer == 3:
                                if DNG > 8:
                                    print ("Wakandans: Mufugguh")
                                    print("The Wakandans are amazed and give you a loan as tribute. You leave the bar with full DONG")
                                    loans = loans +1
                                    dong = DNG
                                if DNG < 9:
                                    print ("Wakandans: HAHAHAHAHA")
                                    print ("Your DONG deflates, and you leave the bar in embarassment")
                                    dong = 0
                        answer = 0
                    if answer == 3:
                        print ("You whip out your DONG and leave the tavern")
                    answer = 0
            if answer == 3:
                print ("You engage your Helicockter on a nearby pedestrian")
                answer = 0
            if answer == 4:
                    print ("You arrive at the residence of Ethota, and find her walking around skimpily while being followed by BETA orbitters")
                    answer = 0
                    while answer < 1 or answer > 2:
                        print ("Ethota: Why do you come here? To pay tribute to my boobs and thottery?")
                        print ("1. Nevermind THOT, I will go now and leave you to your orbiters")
                        print ("2. I wish to join the resistance against the Wakandans")
                        answer = int(input())
                    if answer ==1:
                        answer = 0
                    if answer ==2:
                        if wipipodispo == 3:
                            print ("Ethota: I have heard about how you used your DONG on the Wakandans in the tavern. You have proven yourself, and may join the resistance")
                            answer = 3
                            break
                        if wipipodispo < 3:
                            print ("Ethota: You are not worthy, prove yourself by publicly fighting some Wakandans. For now, face the wrath of my followers. BETAs, get him!")
                            racewar(7,10)
                            answer = 0
def racewarspl(enemy,amount):
        if enemy == 1:
                print ("You have been challenged to battle by ", amount, "straycat")
                #straycat#
                enemyhp=25*amount
                enemystr=5
                enemydng=1*amount
                enemyxp=1*amount
        if enemy == 2:
                print ("You have been challenged to battle by ", amount, "Wakandan Gaurdsmen")
                #Wakandan Gaurdsman#
                enemyhp=35*amount
                enemystr=7
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 3:
                print ("You have been challenged to battle by ", amount, "Beanman")
                #Wakandan Gaurdsman#
                enemyhp=65*amount
                enemystr=8
                enemydng=3*amount
                enemyxp=9*amount
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global DNG
        global exp
        answer = 0
        battleoutcome = 0
        while battleoutcome == 0:
            print ()
            print ("Health:", hp, "/", health)
            print ("DONG:", dong, "/", DNG)
            print ("1. Use Shank")
            print ("2. Use Cialis for DONG (",cialis, ") remaining")
            print ("3. Use Ritalin for health (",ritalin, ") remaining")
            print ("4. Use DONG for special attack")
            answer = int(input())
            if answer == 1:
                damage = random.randrange(1,STR+1,1)
                enemyhp=enemyhp-damage
                print ("You shank the enemy for ", damage, " damage")
            if answer ==2:
                    if cialis > 0:
                        dong=dong+5
                        cialis = cialis - 1
                        if dong > DNG:
                                dong = DNG
                        print ("DONG restored to ", dong, "inches")
                    if cialis == 0:
                        print ("You have no cialis")
            if answer ==3:
                    if ritalin > 0:
                        hp=hp+50
                        ritalin = ritalin - 1
                        if hp > health:
                                hp = health
                        print ("health restored to ", hp, "points")
                    if ritalin == 0:
                        print ("You have no ritalin")
            if answer == 4:
                    if dong >0:
                        damage = random.randrange(5,STR*DNG+5,1)
                        enemyhp=enemyhp-damage
                        print ("You use your dong for ", damage, "damage")
                        dong = dong - 1
                    if dong < 1:
                            print ("Your DONG is not working")
            if enemyhp < 1:
                print ("You have defeated the enemy")
                print ("Exp Gained: ", enemyxp)
                exp = exp + enemyxp
                if exp > (15-INT):
                        print ("You have leveled up")
                        level = level + 1
                        exp = 0
                        strboost = random.randrange(1,3,1)
                        hpboost = random.randrange(1,5,1)
                        dngboost = math.floor(random.randrange(0,5,1)/5)
                        print ("DONG: +", dngboost)
                        print ("Strength: +",strboost)
                        print ("Additional Health: +", hpboost)
                        STR = STR + strboost
                        health = health + hpboost
                        DNG = DNG + dngboost
                        playerstats()
                break
            turns= amount
            while turns > 0:
                damage = random.randrange(0,enemystr+1,1)
                hp=hp-damage
                print ("You are attacked for ", damage, "damage")
                turns=turns-1
            print ("Enemy total Health: ", enemyhp)
            if hp < 1:
                    print ("You have been taken into custody, the Wakandans run train on your ass")
                    hp = health
                    dong = DNG
                    break
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
    INT = int(input("Pick intelligence(1 to 10). Intelligence determines how you can persuade, and how quickly you level"))
AP = AP - INT
print ("Points Left: ", AP)
print ()
playerstats()
if AP < 10:
    while STR < 1 or STR > (AP-1):
        print ("Pick strength (1 to",AP-1,"). Strength contributes to total health and damage.")
        STR = int(input())
if AP > 9:
    while STR < 1 or STR > 10:
        STR = int(input("Pick strength(1 to 10). Strength contributes to total health and damage."))
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
health = 10 * STR + math.floor(DNG/2)
hp = health
dong = DNG
exp = 0
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
    racewar(2, 2)
if answer is 1:
    print ("Tyrone the Gaurdsman: Hunnit dolla round clip muh WE pyramids hotep WE baybamomma (He enjoys your comment, and has decided he will let you in to the city, but only if you entertain him by fighting a stray cat first)")
    racewar(1, 1)
if answer is 3:
    if DNG > 8:
        print("(Tyrone is angered, and draws his UNESCO provided lead pipe as a weapon. Jayvon is frightened by the DONG and runs off into the woods)")
        racewar(2, 1)
    if DNG < 9:
            print ("Tyrone the Gaurdsman: Muh Dick (You are denied intry into Charlottesvisle, you are attacked by the gaurdsmen)")
            racewar(2, 2)
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
    print ("3. How about 100 loans and I promise to touch myself to Wakandan cave paintings later?")
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
        if INT >6:
                loans=  100
                print("Loans: ", loans)
        if INT <7:
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
print ("Beanman: Now hold up. Hrogar, how about we cross DONGs in a sparring match before bed? I will let you lay with my goat afterwards, so you will be healed. No, no, I insist!")
racewar(3, 1)
print ("End of Chapter 1")
hp = health
dong = DNG
playerstats()
##End of Chapter 1##
##saveGame(2)##

##Chapter 2##
print ("Chapter 2: Dindu Nuffin Wrong")
print ("Your sleep is restless, your dreams are full of Wakandans, thousands of them, all riding bicycles that are not theirs. The smell is unimaginable. You are startled awake whenb you realize the smell is real. As you open your eyes, you see a gang of Wakandan Gaurdsmen, led by an officer, heading towards the door to Beanman's")
print()
print ("Nigerius Liberius: Mup da doo bo figly muh kangz whitey Hrogar bo watermellon n sheyit (We have come to requisition all of the supplies of this establishment for the Wakandan army")
print ("Wakandan Gaurdsman: Nigguh (If you fail to comply with this demand, we will issue an arrest warrant on the spot for all those inside, at which point you will be taken to Wakandan court and sent to prison. Disorderly conduct in this Wakandan territory will not be tolerated")
print ("Beanman: You damned Wakandans, these pills and dingy shack are all I have, I will not hand them over willingly")
print ("*Beanman and Bonermere are takend into custody*")
print ()
print ("Nigerius Liberius: Booga Ooga spear chuck malt liquir (You there, Nord, you must come now")
answer = 0
while answer > 3 or answer < 1:
    print ("1. I submit willingly, take me to prison")
    if INT > 7:
        print ("2. [INT] Black Panther was the best movie ever made")
    if INT < 8:
        print ("2. [INT] Uhhhhh, muh dick booga?")
    print ("3. *Show DONG* Fight me, Wakandans")
    print ()
    answer = int(input())
if answer == 1:
        print ("You are taken into custody, the Wakandans run train on your bootyhole")
        prison = 1
if answer == 2:
        if INT > 7:
                print ("Nigerius Liberius: Muh kangz, wipipo cthulu (Indeed it is. You have humored me, Nord, I will let you go")
                prison = 0
        if INT < 8:
                print ("Nigerius Liberius: Muh kangz, wipipo cthulu (Nice try, take him into custody)")
                print ("You are taken into custody, the Wakandans run train on your bootyhole")
                prison = 1
if answer == 3:
        print ("Nigerius Liberius: Nigguh (This insolence will not be tolerated, get him, Wakandans!)")
        print ("Beanman: Take these, Hrogar!")
        print ("Beanman tosses you some pills")
        cialis = cialis + 2
        ritalin = ritalin + 1
        racewarspl (2,3)
        wakandandispo = wakandandispo - 1
        print ("Nigerius knocks you unconscious with his DONG and you are taken to prison")
        prison = 1
print ()
if prison == 0:
        hp = health
        dong = DNG
        print ("Having escaped capture, you are determined to break your colleagues out of Wakandan prison, as prison-breaks are your specialty (in addition to town-raping). You lay with Beanman's goat to restore yourself.")
        print ("After a brief survey of the Wakandan prison, you find a nearby sewer that leads under the walls. The sewer is locked, and you dont have a key")
        answer = 0
        while answer > 2 or answer < 1:
            print ("1. Insert DONG into lock")
            print ("2. Fight nearby gaurd for a key")
            answer = int(input())
            if answer == 1:
                if DNG > 4:
                        print ("You open the lock with your DONG, and are attacked by a stray cat")
                        racewar (1,1)
                if DNG < 5:
                        print ("Nothing happens. A passing Wakandan gaurd notices you fucking a gate and attacks you out of disgust")
                        racewar (2,1)
                        print ("You get the keys and enter the sewers")
            if answer == 2:
                    racewar (2,1)
                    print ("You get the keys and enter the sewers")
        print ("The sewers are dank and smell of malt liquor, you come to a fork in the sewers, with two paths")
        answer = 0
        while answer > 1 or answer < 1:
            print ("1. Go left")
            print ("2. Go right")
            answer = int(input())
            if answer == 2:
                    print ("You find a dead end, and an angry crocodile")
                    racewar (4,1)
        print ("You enter the basement level of the prison and open a grate, revealing a row of cages gaurded by three Wakandan Gaurdsmen. Bonermere's decapitated head sits on a table. Beanman lies in the cell on the corner, and it looks like his ass hurts")
        answer = 0
        while answer > 2 or answer < 1:
            print ("1. Attempt to retrieve Beanman and Bonermere's head")
            print ("2. Attempt to retrieve Beanman")
            answer = int(input())
            if answer ==1:
                    racewar(2,2)
                    print ("You toss Bonermere's head into the sewer. A proper burial")
        print ("You escape with Beanman into the sewers")
        print ("Beanman: Thanks you for saving me, they diddles poor Bonermere to death, I swear I will help you avenge him")
        print ()
if prison == 1:
        print ("You are taken to prison. This being a Wakanda prison, those Wakandans inside are double Wakandans, more fearsome and dumb than the regular ones")
        print ("Bonermere is quickly raped to death upon arrival")
        print ("One of the Double Wakandans breaks from the pack and heads towards you")
        racewar(5,1)
        print ("Beanman: We must find a way out of here")
        answer = 0
        while answer > 2 or answer < 1:
            print ("1. I agree")
            print ("2. I dont know, I kind of like it here")
            answer = int(input())
            if answer ==2:
                    print ("Beanman: Well, I dont have the bootyhole stamina to survive in a place like this")
        print ("Beanman: We must make an attempt to leave before the same fate as Bonermere befalls us. Here, have a ritalin I was able to sneak in, sorry if it tastes like ass.")
        ritalin = ritalin + 1
        answer = 0
        while answer > 2 or answer < 1:
            print ("1. Let me see if I can convince one of these Wakandans to make a distraction")
            if DNG > 7:
                    print ("2. I think I can pick the lock with my DONG")
            if DNG < 8:
                    print ("2. I would pick the lock, but I dont think I have the DONG for it.")
            answer = int(input())
        if answer == 1:
                print("You approach the biggest Wakandan you can find. He seems to be eager, but he requires you to fight him to prove your worth first")
                racewar(5,1)
                print ("The wakandan creates the distraction, allowing you to grab the keys and escape with Beanman into the sewer")
        if answer == 2:
            if DNG > 7:
                    print ("You pick the lock with your DONG and escape with Beanman into the sewers.")
            if DNG < 8:
                    print ("Your DONG does not work. You are attacked by a Wakandan Gaursman, who is disgusted by the sight of you fornicating with the gate>")
                    racewar(2,1)
                    print ("You grab the keys off of the gaurd and escape with Beanman into the sewers.")
print ("Upon exiting the sewers you find a lone goat to restore yourself with. As you finish, you hear a voice")
print ("Nigerius Liberius: Yuh (How have you escaped?? No matter, I will deal with you now, myself!")
hp = health
dong = DNG
racewar(6,1)
print ("You defeat Nigerius Liberius and return to Beanman's Shack to mourn Bonermere")
print ("End of Chapter 2")
print ()
##saveGame(3)##
##End of Chapter 2##

##Start of Chapter 3##
print ("Chapter 3: You KNOW shes got the clap")
print ("Your dreams are of Bonermere and Section 8. The darkness of the Wakandans crowds out the image of his face until there is nothing but void. A dim light appears in the distance. It draws closer and grows in intesity until you are blinded. In a space full of white, you see a Nordic princess, whose skin has turned to leather. She whispers in your ear that none of this would have come to pass if you had just hit her every once in a while. As the world falls apart and you awake, she whispers in your ear: the queefer must awaken")
print ()
print ("You are awakened by Beanman brushing his teeth with the urine from one of his goats")
print ("Beanman: Hrogar, how have you slept?")
answer = 0
while answer > 2 or answer < 1:
            print ("1. I have slept well")
            print ("2. I have slept poorly, this shack smells of goat shit and vape")
            answer = int(input())
if answer ==1:
    print ("Beanman: I should hope so, the mattress you sleep on is made of only the finest goat shit and menthol cigarrette butts")
if answer ==2:
    print ("Beanman: If you dont like it, you can go sleep with the Wakandans and their EBOLA")
print ("Beanman: You look like you could use some supplies")
answer = 0
while answer > 2 or answer < 1:
            print ("1. Yes, my reserves of pills are running low")
            print ("2. I will be fine for now, salad-tosser")
            answer = int(input())
if answer ==1:
    beanman()
if answer ==2:
    print ("Beanman: Suit yourself")
print ()
print ("Beanman: You may want to visit Ethota, she has largely been coordinating the resistance movement against the Wakandans, as the Buttholian government has been infiltrated by Longnoses, and likely will never send us military aid")
ch3roaming()
print ("Ethota: The Wakandans have caused much trouble in the land, and I have used this trouble to satisfy my insatiable lust for attention and money for shoes or whatever the fuck women buy. I have done this by amassing a following of BETAs who see to my every whim. They are strongly anti-Wakandan, buck lack the strenth and DONG to get much done. I need a hero such as yourself to fight for me, and destroy my arch rival, the witch Coalburna, who virtue signals by laying with Wakandans, thus taking attention away from me. This is unacceptable, you must find and destroy this witch. Be warned though, she surrounds herself with Wakandans day and night in her tower at the University of Buttholia. Go now, Hrogar, and slay this whore")
answer = 0
while answer > 2 or answer < 1:
            print ("1. What you do is disgusting. I will help you, but you deserve to be taught some manners first")
            print ("2. *Show DONG* C'mere, Ethota")
            answer = int(input())
if answer ==1:
    print ("Ethota: Fine, but only if I can stream it for my Patreon followers")
    racewar(8,1)
if answer == 2:
    if DNG >7:
        print ("Ethota: BETAs, get the camera, sit in the corner and watch this")
        print (".")
        print (".")
        print (".")
        print (".")
        print (".")
        print (".")
        print (".")
    if DNG <8:
        print ("Ethota: HAHAHAHAHA. You should be embarassed. I will beat you for your pathetic attempt at me")
        racewar(8,1)
print ("End of Chapter 3")
playerstats()

##End of Chapter 3##

#Start of Chapter 4##
print ("Chapter 4: We dont want you back")

