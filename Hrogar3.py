print ("HROGAR 3: Queefs of Change")
import math
import sys
from time import sleep
words = "In the Kangdom of Buttholia, a scourge now grips the land. The Wakandans march accross the Buttholian wheatfields and bring terror and EBOLA to the land. Aided by the Longnoses, the Wakandans have been able to conquer the disputed city of Charlottesvisle, which they have renamed to Section Eight. You are Hrogar, and what you have done in your past does not matter, but if you must know, you are a former prison inmate and town rapist, who was wrongfully imprisoned for being too good at being town rapist. After escaping prison, you have traveled back to your hometown of Charlottesvisle, only to find that it is now Section Eight. The time has Cum for the queefer to awaken."
for char in words:
        sleep(0.00)
        sys.stdout.write(char)
        sys.stdout.flush()
##def racewar(Battle function). Keep monster stats inside battle function so only things to import are monster type and player stats?##
def factiondispo (faction,change):
        if (faction+change) > 2 or (faction+change) < -2:
                break
        if (faction+change) < 3 or (faction+change) > -2:
                faction = faction + change
                break
def playerstats ():
    print ("Name:     Hrogar")
    print ("Race:       Nord")
    print ("Level:        ", level)
    print ("Max Health:   ", 10 * STR + math.floor(DNG/2))
    print ("Intelligence: ", INT)
    print ("Strength:     ", STR)
    print ("DONG:         ", DNG)
playerstats()

#Game Start, to be made function later#
race = 0
level = 0
INT = 0
STR = 0
DNG = 0
y=1
yes = 1
n = 2
no = 2
wakandandispo = -2
longnosedispo = -2
wipipodispo = 1

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

#if chapter(from config file) == 1 :#
print ()
print ("CHAPTER 1: City Gates")
print (" You find yourself at the ancient gates to Charlottesvisle, expecting to see your old friend Bonermere. You instead find a pair of Wakandans gaurdsment blocking your path. Your ebonix is rusty, but they appear to be asking for your travel papers.")
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
if answer is 1:
    print ("Tyrone the Gaurdsman: Hunnit dolla round clip muh WE pyramids hotep WE baybamomma (He enjoys your comment, and has decided he will let you in to the city, but only if you entertain him by fighting a stray cat first)")
    #Battle Function Here, Stray Cat#
if answer is 3:
    if DNG > 8:
        print("(Tyrone is angered, and draws his UNESCO provided lead pipe as a weapon. Jayvon is frightened by the DONG and runs off into the woods)")
        #Battle function here, 1 gaurd#
    if DNG < 9:
            print ("Tyrone the Gaurdsman: Muh Dick (You are denied intry into Charlottesvisle, you are attacked by the gaurdsmen)")
            #Battle Function Here, 2 Gaurds#

