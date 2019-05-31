import math
import sys
import json
#from pprint import pprint
import random
random.seed(a=None, version=2)
#from time import sleep
#import winsound
def askme():
    global answer
    while True:
        try:
            answer = input()
            answer = int(answer)
            break
        except ValueError:
            print("Enter an integer cocksucker")
##Meatperson Temple
##Resistance fighters
##Expand quest generator for different types of quests
gun = 0
health = 0
exp = 0
loans = 0
race =0
level =0
chapter =0
INT = 0
STR = 0
DNG = 0
CHAR=0
hp = 0
dong =0
y=1
yes = 1
n = 2
no = 2
doggo=0
neocheck = 0
armor=0
weapon = "fist"
swipes=1
ATK=1
biome="grasslands"
fame=0
infamy=0
def teambreak():
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global biome
        global armor
        global fame
        global infamy
        answer=0
        while answer<1 or answer>3:
            print("You reach a clearing and consider resting, what do?")
            print("1. Continue onwards")
            print("2. Use pills")
            print("3. Polish ",weapon)
            askme()
        if answer==2:
            answer=0
            while answer < 1 or answer >3:
                print("Use which pill?")
                print("1. Cialis")
                print("2. Ritalin")
                print("3. Nevermind")
                askme()
                if answer ==1:
                        answer=0
                        if cialis > 0:
                            dong=dong+5
                            cialis = cialis - 1
                            if dong > DNG:
                                    dong = DNG
                            print ("DONG restored to ", dong, "inches")
                            #winsound.PlaySound("boing", #winsound.SND_ALIAS)
                        if cialis == 0:
                            print ("You have no cialis")
                if answer ==2:
                        answer=0
                        if ritalin > 0:
                            hp=hp+50
                            ritalin = ritalin - 1
                            if hp > health:
                                    hp = health
                            print ("health restored to ", hp, "points")
                            #winsound.PlaySound("huh", #winsound.SND_ALIAS)
                        if ritalin == 0:
                            print ("You have no ritalin")
                if answer ==3:
                    break
        if answer==3:
            print("You polish your weapon up nicely, its shiny now")
            ATK=ATK+1
def nigglemethis():
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global biome
        global armor
        global fame
        global infamy
        correctans=1
        riddlechance = random.randrange(1,17,1)
        print ("You approach a SPHYNX, and it has a dumb riddle for you")
        if riddlechance == 1:
            print ("What country has agv DONG under 5.3 inches?")
            print ("1. Latvia")
            print ("2. Lebanon")
            print ("3. Indonesia")
            print ("4. Palestine")
            correctans=3
        if riddlechance == 2:
            print ("History has shown which is the ideal candidate for a door whose purpose is to contain gas?")
            print ("1. Wood")
            print ("2. Sealed Steel")
            print ("3. Meat")
            print ("4. Rubber")
            correctans=1
        if riddlechance == 3:
            print ("What is the rainbow typically associated with?")
            print ("1. Butt burglars")
            print ("2. Israel")
            print ("3. Nordic Myth")
            print ("4. Priests")
            correctans=3
        if riddlechance == 4:
            print ("Which instrument is most like the tuba?")
            print ("1. Digeridoo")
            print ("2. your moms ass")
            print ("3. the trumpet")
            print ("4. Palestine")
            correctans=1
        if riddlechance == 5:
            print ("If there are 100000000 bricks on a plane, and one falls off, how many are left?")
            print ("1. 99999999")
            print ("2. 100000000")
            print ("3. 1")
            print ("4. 0")
            correctans=1
        if riddlechance == 6:
            print ("Imagine you're in a dark room that is perfectly empty with nothing in it. There are no windows or doors. What is the easiest way to escape?")
            print ("1. Die")
            print ("2. Stop imagining you are in that room")
            print ("3. Wait")
            print ("4. Jump")
            correctans=2
        if riddlechance == 7:
            print ("Add me to myself and multiply by 4. Divide me by 8 and you will have me once more. What number am I?")
            print ("1. All Numbers")
            print ("2. 32")
            print ("3. 7")
            print ("4. 1")
            correctans=1
        if riddlechance == 8:
            print ("Ripped from my mother's womb. Beaten and burned, I become a bloodthirsty killer. What am I?")
            print ("1. A dragon")
            print ("2. Meat")
            print ("3. Terry")
            print ("4. Iron Ore")
            correctans=4
        if riddlechance == 9:
            print ("It is greater than God and more evil than the devil. The poor have it, the rich need it, and if you eat it you'll die.")
            print ("1. A cactus")
            print ("2. Lebanon")
            print ("3. Nothing")
            print ("4. Everything")
            correctans=3
        if riddlechance == 10:
            print ("With no hammer or any kind of tool I build my house so quickly. What am I?")
            print ("1. Dog")
            print ("2. Congan")
            print ("3. Spider")
            print ("4. The world")
            correctans=3
        if riddlechance == 11:
            print ("I cannot be felt or moved, but as you come closer, I get more distant. What am I?")
            print ("1. Yourself")
            print ("2. Baked Beans")
            print ("3. The woods")
            print ("4. The Horizon")
            correctans=4
        if riddlechance == 12:
            print ("Green arrows grow out of my sides. I go from yellow to white. My babies fly in the wind. What am I?")
            print ("1. Dandelion")
            print ("2. Bears")
            print ("3. The wind")
            print ("4. Beef")
            correctans=1
        if riddlechance == 13:
            print ("I may be made of metal, bone, or wood and have many teeth. My bite hurts no one and the ladies love me. What am I?")
            print ("1. Dog")
            print ("2. Comb")
            print ("3. DONG")
            print ("4. Rings")
            correctans=3
        if riddlechance == 14:
            print ("My parents are singers, and while my father has red hair I am pale and completely bald.")
            print ("1. Yourself")
            print ("2. Egg")
            print ("3. Hills")
            print ("4. A river")
            correctans=2
        if riddlechance == 15:
            print ("Has feathers but can't fly. Rests on legs but can't walk.")
            print ("1. Mattress")
            print ("2. Chicken")
            print ("3. Spider")
            print ("4. DONG")
            correctans=1
        if riddlechance == 16:
            print ("Crooked as a rainbow, and slick as a plate,Ten thousand horses can't pull it straight.")
            print ("1. Dog")
            print ("2. Yourself")
            print ("3. Beer")
            print ("4. River")
            correctans=4
        answer = 0
        while answer >4 or answer <1:
            askme()
        if answer == correctans:
            answer=1
            correctans=1
        if answer != correctans:
            answer=0
def drinkingcomp():
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global biome
        global armor
        global fame
        global infamy
        competition = 1
        round = 1
        while competition == 1:
            print ("Round: ", round)
            if round ==1:
                print ("You drink a beer, it tastes like ass")
                pukechance = random.randrange(1,12,1)
                if pukechance >10:
                    print ("You puke like a bitch, and are raped in the confusion")
                    competition = 0
            if round == 2:
                print ("You drink a beer, it tastes like ass")
                answer = 0
                nigglemethis()
                if answer != 1:
                    print("INCORRECT, You fail")
                    competition = 0
                pukechance = random.randrange(1,12,1)
                if pukechance >10:
                    print ("You puke like a bitch, and are raped in the confusion")
                    competition = 0
            if round == 3:
                print ("You drink a beer, it tastes like ass")
                answer = 0
                print ("What country has agv DONG under 5.3 inches?")
                print ("1. Latvia")
                print ("2. Lebanon")
                print ("3. Israel")
                print ("4. Palestine")
                askme()
                if answer != 3:
                    print("INCORRECT, You fail")
                    competition = 0
                pukechance = random.randrange(1,12,1)
                if pukechance >10:
                    print ("You puke like a bitch, and are raped in the confusion")
                    competition = 0
            if round == 4:
                print ("You drink a beer, it tastes like ass, your vision becomes very blurry and you start to see things")
                print ("Bar Tender: You must fight our pet cat, Mr. Scrubbles")
                print ("You dont see a cat, you go in the alley out back to take a leak")
                randencounter()
                pukechance = random.randrange(1,12,1)
                if pukechance >10:
                    print ("You puke like a bitch, and are raped in the confusion")
                    competition = 0
            if round == 5:
                print ("You drink a beer, it tastes like ass, your vision becomes very blurry and the world spins")
                answer = 0
                nigglemethis()
                if answer != 1:
                    print("INCORRECT, You fail")
                    competition = 0
                pukechance = random.randrange(1,12,1)
                if pukechance >10:
                    print ("You puke like a bitch, and are raped in the confusion")
                    competition = 0
            if round == 6:
                print ("You drink a beer, it tastes like ass, you cant feel your face, the bar seems so far away")
                print ("Mufugguh Bix Noooooood")
                randencounter()
                pukechance = random.randrange(1,12,1)
                if pukechance >10:
                    print ("You puke like a bitch, and are raped in the confusion")
                    competition = 0
            if round == 7:
                print ("You drink a beer, it tastes like ass, you cant feel anything")
                print ("You look into the void, and it looks into you. You are fairly certain the beer your have been drinking contains date rape")
                biome= "woods"
                bossfight(1,1)
                pukechance = random.randrange(1,12,1)
                if pukechance >8:
                    print ("You puke like a bitch, and are raped in the confusion")
                    competition = 0
                if pukechance <9:
                    print("You have won and have gained fame among the townsfolk")
                    fame=fame+1
                    competition=0
            round = round + 1
def looting():
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global biome
        global armor
        global fame
        global infamy
        lootchance=0
        checkone=0
        mweapon=0
        if math.floor(level/10)==0:
            lootchance=4
        if math.floor(level/10)==1:
            lootchance=7
        if math.floor(level/10)==2:
            lootchance=11
        if math.floor(level/10)==3:
            lootchance=15
        if math.floor(level/10)>3:
            lootchance=18
        checkone=random.randrange(0,9,1)
        if checkone <8:
            loot=random.randrange(1,3,1)
        if checkone >7:
            loot=random.randrange(1,lootchance,1)
        if checkone <4:
            loot=0
        if loot ==0:
            print("You find 10 coins in the anus")
            loans=loans+10
        if loot ==1:
            print("You find some pills lying around")
            ritalin=ritalin+1
            cialis=cialis+1
        if loot ==2:
            mweapon="rock"
            mATK=3
            mswipes=1
        if loot ==3:
            mweapon="stick"
            mATK=2
            mswipes=2
        if loot ==4:
            mweapon="siphalitic sword"
            mATK=6
            mswipes=2
        if loot ==5:
            mweapon="siphalitic hammer"
            mATK=14
            mswipes=1
        if loot ==6:
            mweapon="hunnit hi point"
            mATK=2
            mswipes=8
        if loot ==7:
            mweapon="strap on?"
            mATK=3
            mswipes=6
        if loot ==8:
            mweapon="bag of syringes"
            mATK=20
            mswipes=1
        if loot ==9:
            mweapon="actual sword"
            mATK=15
            mswipes=2
        if loot ==10:
            mweapon="actual hammer"
            mATK=32
            mswipes=1
        if loot ==11:
            mweapon="speedy sword"
            mATK=11
            mswipes=3
        if loot ==12:
            mweapon="double headed...hammer"
            mATK=20
            mswipes=2
        if loot ==13:
            mweapon="bag of jew tears"
            mATK=10
            mswipes=5
        if loot ==14:
            mweapon="cerimic elephant knick knack"
            mATK=60
            mswipes=1
        if loot ==15:
            mweapon="Sword of Unintended Sodomy"
            mATK=50
            mswipes=2
        if loot ==16:
            mweapon="hardened meatloaf"
            mATK=80
            mswipes=1
        if loot>1:
            if loot <17:
                print("You have found a ",mweapon,", with ",mATK,"x",mswipes," attack, do you switch with your ",weapon," (",ATK,"x",swipes,")?")
                answer=0
                while answer > 2 or answer < 1:
                    print ("1. Yes")
                    print ("2. No")
                    askme()
                if answer==1:
                    print("You switch weapons")
                    ATK=mATK
                    weapon=mweapon
                    swipes=mswipes
            if loot ==17:
                if gun == 0:
                    print ("You have found a DRILLDO, which you keep along with your normal weapon")
                    gun = 1
def armorlooting():
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global biome
        global armor
        global fame
        global infamy
        lootchance=0
        checkone=0
        mweapon=0
        if math.floor(level/10)==0:
            lootchance=2
        if math.floor(level/10)==1:
            lootchance=4
        if math.floor(level/10)==2:
            lootchance=6
        if math.floor(level/10)==3:
            lootchance=8
        if math.floor(level/10)>3:
            lootchance=9
        loot=random.randrange(0,lootchance+1,1)
        if loot ==0:
            mweapon="t-shirt"
            mATK=2
        if loot ==1:
            mweapon="tye dye shirt"
            mATK=4
        if loot ==2:
            mweapon="potato sack shirt"
            mATK=6
            mswipes=1
        if loot ==3:
            mweapon="leather armor"
            mATK=8
            mswipes=2
        if loot ==4:
            mweapon="Zamak armor"
            mATK=10
            mswipes=2
        if loot ==5:
            mweapon="meat armor"
            mATK=14
            mswipes=1
        if loot ==6:
            mweapon="banana armor"
            mATK=16
            mswipes=8
        if loot ==7:
            mweapon="choker to impress daddy"
            mATK=20
            mswipes=6
        if loot ==8:
            mweapon="syringe armor"
            mATK=24
            mswipes=1
        if loot ==9:
            mweapon="Ungodly armor"
            mATK=26
            mswipes=2
        print("You have found a ",mweapon,", with ",mATK," armor rating, do you switch with your current armor (",armor,")?")
        answer=0
        while answer > 2 or answer < 1:
            print ("1. Yes")
            print ("2. No")
            askme()
            if answer==1:
                print("You switch armor")
                armor=mATK
def randencounter():
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global biome
        global armor
        global fame
        global infamy
        if math.floor(level/10)==0:
            moblvl=6
        if math.floor(level/10)==1:
            moblvl=12
        if math.floor(level/10)==2:
            moblvl=18
        if math.floor(level/10)==3:
            moblvl=24
        if math.floor(level/10)>3:
            moblvl=30
        checkone=random.randrange(1,15,1)
        if checkone<8:
            print("As you make your way through the area you hear footsteps running towards you")
            racewar(random.randrange(1,moblvl),random.randrange(1,3,1))
        if checkone==8:
            print("You find a chest, try to pick with your DONG?")
            answer=0
            while answer > 2 or answer < 1:
                print ("1. Yes")
                print ("2. No")
                askme()
            if answer==1:
                pick=random.randrange(1,DNG,1)
                if pick>4:
                    print("You successfully pick the check with your DONG")
                    looting()
                if pick<5:
                    print("You hurt your DONG and do not open the lock")
                    dong=1
                print("1.OKAY")
                askme()
                answer = 0
        if checkone==9:
            print("You take a nap and are robbed, you lost some coins, but strangely your DONG is at full mast")
            dong=DNG
            loans=loans-10
            if loans <0:
                loans=0
            print("1.OKAY")
            askme()
            answer = 0
        if checkone==10:
            print("You find a bag of pills, take the pills?")
            answer=0
            while answer > 2 or answer < 1:
                print ("1. Yes")
                print ("2. No")
                askme()
            if answer==1:
                pillchance=random.randrange(1,3,1)
                if pillchance==3:
                    print("You are completely healed by the random pills, and stiffer than usual")
                    hp=health
                    dong=DNG+1
                if pillchance<3:
                    print("Pill were really marbles, you puke and are molested in the confusion, you lose some health")
                    hp=hp-10
                    if hp<1:
                        hp=1
                print("1.OKAY")
                askme()    
                answer = 0
        if checkone==11:
            print("You trip and stumble")
            answer = 0
            while answer <1 or answer >2:
                print("How do you try to recover?")
                print("1. Use DONG")
                print("2. Just fall and take it")
                askme()
            if answer ==1:
                if dong < 6:
                    print("Your DONG does nothing to stop the fall")
                    if hp > 11:
                        hp=hp-10
                    if hp < 11:
                        hp=1
                if dong >5:
                    print("Your DONG stops the fall and you rebound gracefully")
                    answer = input("1.OKAY")      
                    answer = 0
            if answer ==2:
                print("You fall and look retarded")
            answer = input("1.OKAY")      
            answer = 0
        if checkone==12:
            print("You come across a lone goat, what do you do?")
            answer=0
            while answer >3 or answer <1:
                print("1. Continue onwards")
                print("2. Lay with goat")
                print("3. throw money at goat")
                askme()
            if answer==2:
                print("The goat was really a cat, no pussy for you")
                racewar(1,1)
            if answer==3:
                print("You throw coins at the goat and inspect it")
                loans=loans-10
                if loans <0:
                    loans =0
                looting()
            answer = input("1.OKAY")      
            answer = 0
        if checkone==12:
            print("You find a man passed out with booze in his hand, what do you do?")
            answer=0
            while answer >3 or answer <1:
                print("1. Continue onwards")
                print("2. Loot the drunkard")
                print("3. Attack drunkard")
                askme()
            if answer== 2 or answer ==3:
                print("He awakes and attacks you")
                racewar(9,1)
        if checkone==13:
            print("You see something shiny on the ground ahead of you, investigate?")
            answer=0
            while answer >2 or answer <1:
                print("1. Yes")
                print("2. No")
                askme()
            if answer==1:
                shinychance=random.randrange(1,4,1)
                if shinychance==1:
                    print("It was nothing, just some dirt")
                if shinychance==2:
                    print("Its your lucks day, it was a coin")
                    loans=loans+1
                if shinychance==3:
                    print("Its a rock, but, like, a cool rock. You leave it there to be cool")
            answer = input("1.OKAY")
            answer = 0
        if checkone==14:
            nigglemethis()
            if answer ==1:
                print ("You correctly answer the riddle and proceed forwards")
            if answer ==0:
                print ("You are incorrect and are attacked")
                racewar(random.randrange(1,moblvl),random.randrange(1,3,1))
def bossfight(enemy,amount):
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global biome
        global armor
        global fame
        global infamy
        if biome == "grasslands":
                print ("You reach a clearing in the grasses, the wind blows and you hear a low rumble, you are attacked by a Grass Golem")
                #winsound.PlaySound("strayCatSound", #winsound.SND_ALIAS)
                enemyhp=health+15
                enemystr=STR+5
                enemydng=3
                enemyxp=12
                amount=2
                appendage="grass whistle"
        if biome == "cave":
                print ("You reach the back of the cave, the cave trembles and you fear an earthquake, you are assaulted by a Rock Monster, but not like the gay B-52 kind")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=health+15
                enemystr=STR
                enemydng=3
                enemyxp=12
                amount=3
                appendage="rock hard appendage"
        if biome == "woods":
                print ("You see a large tree begin to move towards you, and realize it is alive. You are attacked by a Dryad, and he has WOOD for you")
                #winsound.PlaySound("beanMan", #winsound.SND_ALIAS)
                enemyhp=health+15
                enemystr=STR+7
                enemydng=3
                enemyxp=12
                amount=1
                appendage="BIG WOOD"
        if biome == "ruins":
                print ("You reach a collapsed temple, and from the rubble comes a Mutant Bear, it attacks you immediately with its BEAR DONG")
                #winsound.PlaySound("beanMan", #winsound.SND_ALIAS)
                enemyhp=health+15
                enemystr=STR+5
                enemydng=3
                enemyxp=12
                amount=2
                appendage="BEAR DONG"
        if biome == "island":
                print ("You hear a strange sound, and suddenly you find yourself attacked by a CRAB RAVE")
                #winsound.PlaySound("doubleWakandan", #winsound.SND_ALIAS)
                enemyhp=health+15
                enemystr=math.floor(STR/4)+1
                enemydng=3
                enemyxp=12
                amount=5
                appendage="claw"
        answer = input("1.OKAY")      
        answer = 0
        battleoutcome = 0
        while battleoutcome == 0:
            print ()
            print ("Health:", hp, "/", health)
            print ("DONG:", dong, "/", DNG,"   ",end ="")
            countr=dong
            print("8", end ="")
            while countr > 0:
                print("=", end ="") 
                countr = countr-1
            print ("D")
            print ("1. Use ",weapon)
            print ("2. Use Cialis for DONG (",cialis, ") remaining")
            print ("3. Use Ritalin for health (",ritalin, ") remaining")
            print ("4. Use DONG for special attack")
            print ("5. 'Charm' your opponent")
            if gun == 1:
                print ("6. Use DRILLDO")
            askme()
            if answer == 1:
                turns= swipes
                while turns > 0:
                    damage = random.randrange(0,STR+2*ATK,1)
                    enemyhp=enemyhp-damage
                    print ("You attack the enemy for ", damage, " damage")
                    #winsound.PlaySound("shank", #winsound.SND_ALIAS)
                    turns=turns-1
                if doggo ==1:
                    doggodamage = random.randrange(0,STR,1)
                    enemyhp = enemyhp - doggodamage
                    print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                    #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if answer ==2:
                    if cialis > 0:
                        dong=dong+5
                        cialis = cialis - 1
                        if dong > DNG:
                                dong = DNG
                        print ("DONG restored to ", dong, "inches")
                        #winsound.PlaySound("boing", #winsound.SND_ALIAS)
                    if cialis == 0:
                        print ("You have no cialis")
                    if doggo ==1:
                        doggodamage = random.randrange(0,STR,1)
                        enemyhp = enemyhp - doggodamage
                        print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                        #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if answer ==3:
                    if ritalin > 0:
                        hp=hp+50
                        ritalin = ritalin - 1
                        if hp > health:
                                hp = health
                        print ("health restored to ", hp, "points")
                        #winsound.PlaySound("huh", #winsound.SND_ALIAS)
                    if ritalin == 0:
                        print ("You have no ritalin")
                    if doggo ==1:
                        doggodamage = random.randrange(0,STR,1)
                        enemyhp = enemyhp - doggodamage
                        print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                        #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if answer == 4:
                    if dong >0:
                        damage = random.randrange(STR,STR*3+20,1)
                        enemyhp=enemyhp-damage
                        print ("You use your DONG for ", damage, "damage")
                        #winsound.PlaySound("getHit", #winsound.SND_ALIAS)
                        dong = dong - 1
                    if dong < 1:
                            print ("Your DONG is not working")
                    if doggo ==1:
                        doggodamage = random.randrange(0,STR,1)
                        enemyhp = enemyhp - doggodamage
                        print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                        #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if answer == 5:
                    charmchance=random.randrange(1,10+CHAR,1)
                    if charmchance > 10:
                        charmchance = random.randrange(0,17,1)
                        if charmchance >10:
                            print ("You empty the balls of the enemy, but it only makes them angrier")
                            asdf=input("1. OKAY")
                    if charmchance < 11:
                        print ("You fail to charm the enemy")
            if answer == 6:
                    if gun == 1:
                        damage = random.randrange(20,30*INT,1)
                        enemyhp=enemyhp-damage
                        print ("You use your DRILLDO for ", damage, "damage")
                        #winsound.PlaySound("useDrilldo", #winsound.SND_ALIAS)
                    if doggo ==1:
                        doggodamage = random.randrange(0,STR,1)
                        enemyhp = enemyhp - doggodamage
                        print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                        #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if enemyhp < 1:
                print ("You have defeated the enemy")
                looting()
                looting()
                looting()
                armorlooting()
                print ("Exp Gained: ", enemyxp)
                exp = exp + enemyxp
                coinss = random.randrange(0,enemyxp*2,1)
                print ("You have gained ", coinss, " coins from the wallet")
                loans = loans + coinss
                while exp > (16-INT):
                        print ("You have leveled up")
                        #winsound.PlaySound("levelUp", #winsound.SND_ALIAS)
                        level = level + 1
                        exp = exp - (16-INT)
                        strboost = random.randrange(1,3,1)
                        hpboost = random.randrange(1,8,1)
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
                dongchance = random.randrange(1,7,1)
                if dongchance < 5:
                    damage = random.randrange(0,math.floor((enemystr)*(100-armor)/100)+1,1)
                    hp=hp-damage
                    print ("You are attacked for ", damage, "damage")
                    ##winsound.PlaySound("getHit", #winsound.SND_ALIAS)
                if dongchance > 4:
                    damage = random.randrange(3,math.floor((enemystr)*(100-armor)/100)+4,1)
                    hp=hp-damage
                    print ("You are attacked with a",appendage," for ", damage, "damage")
                    #winsound.PlaySound("getDonged", #winsound.SND_ALIAS)
                turns=turns-1
            print ("Enemy total Health: ", enemyhp)
            if hp < 1:
                    print ("You have died, the enemy diddles your corpse")
                    print ("GAME OVER")
                    youdednigga=input()
                    while health > 0:
                            print ("Game Over Loser")
def racewar(enemy,amount):
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global biome
        global armor
        global fame
        global infamy
        if enemy == 1:
                print ("You have been challenged to battle by ", amount, "straycat")
                #straycat#
                #winsound.PlaySound("strayCatSound", #winsound.SND_ALIAS)
                enemyhp=25*amount
                enemystr=5
                enemydng=1*amount
                enemyxp=1*amount
        if enemy == 2:
                print ("You have been challenged to battle by ", amount, "Gaurdsmen")
                #Wakandan Gaurdsman#
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 3:
                print ("You have been challenged to battle by ", amount, "Woodsman")
                #Beanman#
                #winsound.PlaySound("beanMan", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=9
                enemydng=3*amount
                enemyxp=9*amount
        if enemy == 4:
                print ("You have been challenged to battle by ", amount, "crocodile")
                #Crocodile#
                #winsound.PlaySound("beanMan", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=11
                enemydng=1*amount
                enemyxp=3*amount
        if enemy == 5:
                print ("You have been challenged to battle by ", amount, "Double Gaurd")
                #Double Wakandan#
                #winsound.PlaySound("doubleWakandan", #winsound.SND_ALIAS)
                enemyhp=60*amount
                enemystr=12
                enemydng=1*amount
                enemyxp=4*amount
        if enemy == 6:
                print ("You have been challenged to battle by ", amount, "Knight")
                #Nigerius Liberius#
                #winsound.PlaySound("nigeriusLiberius", #winsound.SND_ALIAS)
                enemyhp=100*amount
                enemystr=15
                enemydng=1*amount
                enemyxp=9*amount
        if enemy == 7:
                print ("You have been challenged to battle by ", amount, "Beta Orbiters")
                #Beta Orbiter#
                #winsound.PlaySound("betaOrbiters", #winsound.SND_ALIAS)
                enemyhp=2*amount
                enemystr=1
                enemydng=1*amount
                enemyxp=1
        if enemy == 8:
                print ("You have been challenged to battle by ", amount, "Lauren Southern")
                #Ethota#
                #winsound.PlaySound("laurenS", #winsound.SND_ALIAS)
                enemyhp=120*amount
                enemystr=18
                enemydng=1*amount
                enemyxp=9
        if enemy == 9:
                print ("You have been challenged to battle by ", amount, "Drunken Peasant")
                #Drunken Peasant#
                #winsound.PlaySound("drunkenPeasant", #winsound.SND_ALIAS)
                enemyhp=70*amount
                enemystr=10
                enemydng=1*amount
                enemyxp=3*amount
        if enemy == 10:
                print ("You have been challenged to battle by ", amount, "Mr. Sniffles the cat")
                #Super Cat#
                #winsound.PlaySound("misterNiggles", #winsound.SND_ALIAS)
                enemyhp=70*amount
                enemystr=10
                enemydng=1*amount
                enemyxp=3*amount
        if enemy == 11:
                print ("You have been challenged to battle by ", amount, "Ghost")
                #Ghost of Nigerius Liberius#
                #winsound.PlaySound("ghostOfNigLib", #winsound.SND_ALIAS)
                enemyhp=100*amount
                enemystr=15
                enemydng=1*amount
                enemyxp=5*amount
        if enemy == 12:
                print ("You have been challenged to battle by ", amount, "DoppleBonermere")
                #Dopple Hrogar#
                #winsound.PlaySound("doppleHrogar", #winsound.SND_ALIAS)
                enemyhp=health
                enemystr=STR+3
                enemydng=DNG
                enemyxp=9*amount
        if enemy == 13:
                print ("You have been challenged to battle by ", amount, "Abomination")
                #Nigglet#
                #winsound.PlaySound("niglet", #winsound.SND_ALIAS)
                enemyhp=6*amount
                enemystr=1
                enemydng=1
                enemyxp=9
        if enemy == 14:
                print ("You have been challenged to battle by ", amount, "Roastie")
                #Coalburna#
                #winsound.PlaySound("coalBurna", #winsound.SND_ALIAS)
                enemyhp=200*amount
                enemystr=24
                enemydng=1
                enemyxp=20
        if enemy == 15:
                print ("You have been challenged to battle by the king of kangs")
                #NIGGUS GIGGUS#
                #winsound.PlaySound("niggusGiggus", #winsound.SND_ALIAS)
                enemyhp=650*amount
                enemystr=50
                enemydng=1
                enemyxp=50
        if enemy == 16:
                print ("You have been challenged to battle by ", amount, "Fupanoceros")
                #Fupanoceros#
                #winsound.PlaySound("fatGirl", #winsound.SND_ALIAS)
                enemyhp=300*amount
                enemystr=10
                enemydng=1
                enemyxp=10
        if enemy == 17:
                print ("You have been challenged to battle by ", amount, "Neocon")
                #Neocon#
                #winsound.PlaySound("neoCon", #winsound.SND_ALIAS)
                enemyhp=80*amount
                enemystr=15
                enemydng=1
                enemyxp=3*amount
        if enemy == 18:
                print ("You have been challenged to battle by ", amount, "George H.W. Acorn Pecker")
                #Bush#
                #winsound.PlaySound("gwBush", #winsound.SND_ALIAS)
                enemyhp=200
                enemystr=25
                enemydng=1
                enemyxp=10
        if enemy == 19:
                print ("You have been challenged to battle by the SSG BRAWLY")
                #BRAWLY#
                #winsound.PlaySound("beanMan", #winsound.SND_ALIAS)
                enemyhp=1500*amount
                enemystr=120
                enemydng=1
                enemyxp=1
        if enemy == 20:
                print ("You have been challenged to battle by ", amount, "Gaurdsmen")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 21:
                print ("You have been challenged to battle by ", amount, "wolf")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 22:
                print ("You have been challenged to battle by ", amount, "land octopus")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 23:
                print ("You have been challenged to battle by ", amount, "grizzle snake")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 24:
                print ("You have been challenged to battle by ", amount, "rhino")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 25:
                print ("You have been challenged to battle by ", amount, "small dragon")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 26:
                print ("You have been challenged to battle by ", amount, "sentient bean burrito")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 27:
                print ("You have been challenged to battle by ", amount, "retarded puppy")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 28:
                print ("You have been challenged to battle by ", amount, "regular bear")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 29:
                print ("You have been challenged to battle by ", amount, "mutant cannibal")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 30:
                print ("You have been challenged to battle by ", amount, "demon")
                #winsound.PlaySound("wakandanGuardsman", #winsound.SND_ALIAS)
                enemyhp=35*amount
                enemystr=6
                enemydng=4*amount
                enemyxp=2*amount
        if enemy == 98:
                print ("You have been attacked by the drifter")
                #drifter#
                #winsound.PlaySound("wakandanGaurdsman", #winsound.SND_ALIAS)
                enemyhp=40
                enemystr=1
                enemydng=1
                enemyxp=12
        if enemy == 99:
                print ("You have been attacked for your heinous act")
                #NPC#
                #winsound.PlaySound("beanMan", #winsound.SND_ALIAS)
                enemyhp=40
                enemystr=10
                enemydng=1
                enemyxp=1
        answer = input("1.OKAY")      
        answer = 0
        battleoutcome = 0
        while battleoutcome == 0:
            print ()
            print ("Health:", hp, "/", health)
            print ("DONG:", dong, "/", DNG,"   ",end ="")
            countr=dong
            print("8", end ="")
            while countr > 0:
                print("=", end ="") 
                countr = countr-1
            print ("D")
            print ("1. Use ",weapon)
            print ("2. Use Cialis for DONG (",cialis, ") remaining")
            print ("3. Use Ritalin for health (",ritalin, ") remaining")
            print ("4. Use DONG for special attack")
            print ("5. 'Charm' your opponent")
            if gun == 1:
                print ("6. Use DRILLDO")
            askme()
            if answer == 1:
                turns= swipes
                while turns > 0:
                    damage = random.randrange(0,2*STR+2*ATK,1)
                    enemyhp=enemyhp-damage
                    print ("You attack the enemy for ", damage, " damage")
                    #winsound.PlaySound("shank", #winsound.SND_ALIAS)
                    turns=turns-1
                if doggo ==1:
                    doggodamage = random.randrange(0,STR,1)
                    enemyhp = enemyhp - doggodamage
                    print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                    #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if answer ==2:
                    if cialis > 0:
                        dong=dong+5
                        cialis = cialis - 1
                        if dong > DNG:
                                dong = DNG
                        print ("DONG restored to ", dong, "inches")
                        #winsound.PlaySound("boing", #winsound.SND_ALIAS)
                    if cialis == 0:
                        print ("You have no cialis")
                    if doggo ==1:
                        doggodamage = random.randrange(0,STR,1)
                        enemyhp = enemyhp - doggodamage
                        print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                        #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if answer ==3:
                    if ritalin > 0:
                        hp=hp+50
                        ritalin = ritalin - 1
                        if hp > health:
                                hp = health
                        print ("health restored to ", hp, "points")
                        #winsound.PlaySound("huh", #winsound.SND_ALIAS)
                    if ritalin == 0:
                        print ("You have no ritalin")
                    if doggo ==1:
                        doggodamage = random.randrange(0,STR,1)
                        enemyhp = enemyhp - doggodamage
                        print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                        #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if answer == 4:
                    if dong >0:
                        damage = random.randrange(STR,STR*3+25,1)
                        enemyhp=enemyhp-damage
                        print ("You use your DONG for ", damage, "damage")
                        #winsound.PlaySound("getHit", #winsound.SND_ALIAS)
                        dong = dong - 1
                    if dong < 1:
                            print ("Your DONG is not working")
                    if doggo ==1:
                        doggodamage = random.randrange(0,STR,1)
                        enemyhp = enemyhp - doggodamage
                        print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                        #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if answer == 5:
                    charmchance=random.randrange(1,13+CHAR,1)
                    if charmchance > 10:
                        charmchance = random.randrange(0,19,1)
                        if charmchance >10:
                            print ("You empty the balls of the enemy and flee")
                            asdf=input("1. OKAY")
                            battleoutcome = 1
                            break
                    if charmchance < 11:
                        print ("You fail to charm the enemy")
            if answer == 6:
                    if gun == 1:
                        damage = random.randrange(20,30*INT,1)
                        enemyhp=enemyhp-damage
                        print ("You use your DRILLDO for ", damage, "damage")
                        #winsound.PlaySound("useDrilldo", #winsound.SND_ALIAS)
                    if doggo ==1:
                        doggodamage = random.randrange(0,STR,1)
                        enemyhp = enemyhp - doggodamage
                        print ("Frisky Pete attacks with his DONG for ", doggodamage, " damage")
                        #winsound.PlaySound("friskyPete", #winsound.SND_ALIAS)
            if enemyhp < 1:
                print ("You have defeated the enemy")
                looting()
                print ("Exp Gained: ", enemyxp)
                exp = exp + enemyxp
                coinss = random.randrange(0,enemyxp*2,1)
                print ("You have gained ", coinss, " coins from the wallet")
                loans = loans + coinss
                while exp > (16-INT):
                        print ("You have leveled up")
                        #winsound.PlaySound("levelUp", #winsound.SND_ALIAS)
                        level = level + 1
                        exp = exp - (16-INT)
                        strboost = random.randrange(1,3,1)
                        hpboost = random.randrange(1,8,1)
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
                    damage = random.randrange(0,math.floor((enemystr)*(100-armor)/100)+1,1)
                    hp=hp-damage
                    print ("You are attacked for ", damage, "damage")
                    ##winsound.PlaySound("getHit", #winsound.SND_ALIAS)
                if dongchance > 4:
                    damage = random.randrange(3,math.floor((enemystr)*(100-armor)/100)*2+2,1)
                    hp=hp-damage
                    print ("You are attacked with a DONG for ", damage, "damage")
                    #winsound.PlaySound("getDonged", #winsound.SND_ALIAS)
                turns=turns-1
            print ("Enemy total Health: ", enemyhp)
            if hp < 1:
                    print ("You have died, the enemy diddles your corpse")
                    print ("GAME OVER")
                    youdednigga=input()
                    while health > 0:
                            print ("Game Over Loser")
def playerstats ():
    print ("Name:     Bonermere")
    print ("Race:       ",race)
    print ("Gold:         ", loans)
    print ("Level:        ", level)
    print ("Max Health:   ", health)
    print ("Intelligence: ", INT)
    print ("Strength:     ", STR)
    print ("DONG:         ", DNG)
    print ("Charisma:     ", CHAR)
    print ( )
def beanman():
        global loans
        global cialis
        global ritalin
        global hp
        global dong
        global answer
        global INT
        global ATK
        wipipodispo=0
        if wipipodispo == -2:
                print ("Beanman: I dont serve traitors like you")
        if wipipodispo > -2:
                answer = 0
                while answer > 6 or answer < 6:
                    print ("Hand Rubbing Merchant: Well hello there, you look like you could use some supplies, take a look at these wares")
                    print ()
                    print ("Gold:       ", loans)
                    print ()
                    print ("1. [100 Gold] *Buy Wheaties to increase intelligence*")
                    print ("2. [15 Gold] *Buy Ritalin* Can be used to restore 50 Health)")
                    print ("3. [5 Gold] *Buy Cialis* (Can be used to restore DONG)")
                    print ("4. [3 Gold] *Diddle Communal Goat* (Restores Health and DONG)")
                    print ("5. [100 Gold] *Have merchant polish your...weapon")
                    print ("6. *Show DONG*(and then leave the shop)")
                    askme()
                    if answer ==1:
                        if loans > 99:
                            if INT>10:
                                print("Beanman: You are already to smart, the wheaties will only bloat you")
                            if INT<11:
                                print("Beanman: You eat the Wheaties and get smarterer")
                                INT=INT+1
                                loans=loans-100
                        if loans <100:
                            print ("Beanman: You trying to get a heart attack? You cant afford it anyways")
                    if answer ==2:
                        if loans > 14:
                                ritalin = ritalin + 1
                                loans = loans - 15
                                print ("*You receive a ritalin*")
                                print ()
                        if loans < 15:
                                print ("Beanman: You poor bastard, come back with some gold")
                                print ()
                    if answer == 3:
                        if loans > 4:
                                cialis = cialis + 1
                                loans = loans - 5
                                print ("*You receive a cialis*")
                                print ()
                        if loans < 5:
                                print ("Beanman: You poor bastard, come back with some gold")
                                print ()
                    if answer == 4:
                        if loans > 2:
                                hp = health
                                dong = DNG
                                loans = loans - 3
                                print ("*You go to work on that goat, youre a goddamned picasso of goat diddling*")
                                print ()
                        if loans < 5:
                                print ("Beanman: You poor bastard, come back with some gold")
                                print()
                    if answer == 5:
                        if loans > 99:
                                ATK=ATK+5
                                loans = loans - 100
                                print ("*The merchant polishes your weapon, its part of his job, but you notice he seems to be particularly enjoying his work*")
                                print ()
                        if loans < 100:
                                print ("Beanman: You poor bastard, come back with some gold")
                                print()
                    if answer == 6:
                        print ("You leave the shop")
                        break

def questbuilder():
    global hp
    global health
    global dong
    global dng
    global cialis
    global ritalin
    global level
    global STR
    global INT
    global DNG
    global exp
    global loans
    global gun
    global doggo
    global answer
    global weapon
    global ATK
    global swipes
    global CHAR
    global race
    global biome
    global armor
    global fame
    global infamy
    biome="grasslands"
    npcname="Buttmax"
    npcnamel="Bloatmaxx"
    biomechance = random.randrange(1,6,1)
    firstnamechance = random.randrange(1,21,1)
    lastnamechance = random.randrange(1,11,1)
    if biomechance == 1:
        biome="grasslands"
    if biomechance == 2:
        biome="cave"
    if biomechance == 3:
        biome="woods"
    if biomechance == 4:
        biome="ruins"
    if biomechance == 5:
        biome="island"
    if firstnamechance==1:
        npcname="Kieth"
    if firstnamechance==2:
        npcname="Ephebophilus"
    if firstnamechance==3:
        npcname="Assman"
    if firstnamechance==4:
        npcname="Yuzu"
    if firstnamechance==5:
        npcname="Yamada"
    if firstnamechance==6:
        npcname="Giffin 'the big gay'"
    if firstnamechance==7:
        npcname="Leftnut"
    if firstnamechance==8:
        npcname="Mogarth"
    if firstnamechance==9:
        npcname="Adam"
    if firstnamechance==10:
        npcname="Diddler"
    if firstnamechance==11:
        npcname="Molestus"
    if firstnamechance==12:
        npcname="Impotentus"
    if firstnamechance==13:
        npcname="Obese"
    if firstnamechance==14:
        npcname="Very Gay"
    if firstnamechance==15:
        npcname="Possiblyghey"
    if firstnamechance==16:
        npcname="Goattoucher"
    if firstnamechance==17:
        npcname="Longdong"
    if firstnamechance==18:
        npcname="Shaniqua"
    if firstnamechance==19:
        npcname="Tyrone"
    if firstnamechance==20:
        npcnamel="Tartarus"
    if lastnamechance==1:
        npcnamel="Ephebophilus"
    if lastnamechance==2:
        npcnamel="Dindunuffin"
    if lastnamechance==3:
        npcnamel="Notgaypriest"
    if lastnamechance==4:
        npcnamel="Mellonsitter"
    if lastnamechance==5:
        npcnamel="YuriJerker"
    if lastnamechance==6:
        npcnamel="Perez"
    if lastnamechance==7:
        npcnamel="Rightnut"
    if lastnamechance==8:
        npcnamel="Greenberg"
    if lastnamechance==9:
        npcnamel="Chodilus"
    if lastnamechance==10:
        npcnamel="Metrocarpet"
    thelost = random.randrange(1,9,1)
    if thelost ==1:
        thelost = "waifu"
    if thelost ==2:
        thelost = "talking fleshlight"
    if thelost ==3:
        thelost = "credentials to my encrypted loli folder"
    if thelost ==4:
        thelost = "family pet/concubine"
    if thelost ==5:
        thelost = "bag of ordinary dirt"
    if thelost ==6:
        thelost = "wife's son"
    if thelost ==7:
        thelost = "donations meant for Bernie Sanders"
    if thelost ==8:
        thelost = "sweet roll"
    wronging = random.randrange(1,4,1)
    if wronging==1:
        wrongs="taken"
    if wronging==2:
        wrongs="killed"
    if wronging==3:
        wrongs="diddled"
    halping = random.randrange(1,4,1)
    if halping ==1:
        halp=" and I have need of your services,"
    if halping ==2:
        halp=" and your skills and DONG match my needs,"
    if halping ==3:
        halp=" and I am willing to pay gold if you help me,"
    lastwords=random.randrange(1,4,1)
    if lastwords ==1:
        lasword=" I require social justice to be done."
    if lastwords ==2:
        lasword=" My friends and family have disowned me, I have no one else to turn to. "
    if lastwords ==3:
        lasword=" This mistake was my own and entirely avoidable if I had not done bath salts. "
    print (npcname,npcnamel," : You there, " , race," my name is ", npcname," ",npcnamel,halp," you see, my ",thelost," was ",wrongs," by beasts who proceded to take the remains of my ",thelost," to the ",biome," located here on this map.",lasword," Please, can you go to these ",biome,"s and avenge my ",thelost,"?")
    print(" ")
    print(" ")
    answer=0
    while answer < 1 or answer >2:
        print("Will you go to the",biome,"to help ",npcname,"?")
        print("1. Yes")
        print("2. No")
        askme()
    if answer==2:
        print("You choose to not assist")
    if answer==1:
        print("You decide to assist. Visit the market before leaving?")
        print("1. Yes")
        print("2. No")
        answer=0
        while answer < 1 or answer >2:
            askme()
        if answer==1:
            beanman()
        if answer==2:
            print("You decide to leave right away")
            print("1.OKAY")
            askme()
        if biomechance == 1:
            print("You arrive at the grasslands, a wild place of grass and land, you proceed onward, remembering the promise to ",npcname)
        if biomechance == 2:
            print("You finally get to the cave, a dark hole smelling of sulfur, you wonder why you agreed to help ",npcname)
        if biomechance == 3:
            print("You come to the woods, they are full of bugs, but you want to help ",npcname)
        if biomechance == 4:
            print("You find the ruins of western civilization, at one point called 'Detroit', a dark hole smelling of sulfur, you wonder why you agreed to help ",npcname)
        if biomechance == 5:
            print("You reach the island its nice, you are glad ",npcname," isnt here to ruin it")
        asdf=input("1.OKAY")
        randencounter()
        randencounter()
        print("You progress deeper into the ",biome)
        asdf=input("1.OKAY")
        randencounter()
        teambreak()
        randencounter()
        randencounter()
        teambreak()
        bossfight(1,1)
        if biomechance == 1:
            print("You defeat the grass monster and see ",thelost," laying there amongst the grass")
        if biomechance == 2:
            print("Having overcome the rock monster and his appendage, you find ammist the rubble ",thelost," slightly dirty but largely intact")
        if biomechance == 3:
            print("From inside of the trunk of the Dryad,you find ",thelost," laying there with splinters and a bonner")
        if biomechance == 4:
            print("You defeat the bear and find ",thelost," laying there in the bears guts")
        if biomechance == 5:
            print("You defeat the CRAB RAVE and see ",thelost," laying there amongst the grass")
        print(" ")
        answer=0
        while answer < 1 or answer >3:
            print("Will you bring the",thelost,"back to",npcname,"?")
            print("1. Yes")
            print("2. No")
            print("3. Defile ",thelost)
            askme()
        if answer==1:
            print("You decide to do right by ",npcname,npcnamel)
            print("1.OKAY")
            askme()
            print("Upon your arrival into town, you are greeted eagerly by ",npcname)
            print(npcname,npcnamel,": I am so glad you have returned, please, take this coin as a token of my gratitude, and you may also lay with my wife")
            loans=loans+50
            fame=fame+1
            print("1.OKAY")
            askme()
        if answer==2:
            print("You decide to leave empty handed")
            print("1.OKAY")
            askme()
            print("Upon your arrival into town, you are greeted eagerly by ",npcname)
            print(npcname,npcnamel,":I am glad to see you have returned, but where is my ",thelost,"?")
            answer=0
            while answer < 1 or answer >2:
                print("1. I did not retrieve it")
                print("2. I have em right here[lie]")
                askme()
            print(npcname,npcnamel,": You are empty handed, why did you get my hopes up? I will now commit sudoku")
            print("1.OKAY")
            askme()
            answer=0
        if answer==3:
            print("You go to town on the",thelost)
            print("1.OKAY")
            askme()
            print("Upon your arrival into town, you are greeted eagerly by ",npcname)
            print(npcname,npcnamel,":I am glad to see you have returned, but where is my ",thelost,"?")
            answer=0
            while answer < 1 or answer >2:
                print("1. I did not retrieve it")
                print("2. I defiled it, was very enjoyable")
                askme()
            print(npcname,npcnamel,": You did what?! I will kill you for this")
            racewar(99,1)
            infamy=infamy+1
            answer=0
answer = 0
##Chapter 0
print("AssMaster Studios Presents: BONERMERE: rise of the diddler")
print("In a time long before the take over of Charlottesvisle, the simple land of the west continued on without a care for the troubles of the world. You are Bonermere, an adventurer whose fate is yet to be determined. You were recently a simple goat fondler, who has turned his back on his father's profession to see the world. You come to the town of False-crutch, amd seek to make a name for yourself. The town is full of yuppies, but there is work to be had, for those brave enough....")
while answer >4 or answer <1: 
    print("Pick your race (Mutt=1, Booga = 2, Meatperson = 3, Low T Beta = 4:  ")
    askme()
print ()

if answer == 1:
    print ("Oh, so you are a Mutt then? Paying someone elses toll")
    baseINT=1
    baseCHAR=2
    baseSTR=2
    baseDNG=1
    race="Mutt"
    print ()
if answer == 2:
    print ("Oh, so you are a Booga then? The Popeyes is a block that way")
    baseINT=0
    baseCHAR=1
    baseSTR=3
    baseDNG=2
    race="Booga"
    print ()
if answer == 3:
    print ("Oh, so you are a Meatperson then? You look like kindling to me?")
    baseINT=3
    baseCHAR=2
    baseSTR=0
    baseDNG=0
    race="Meatperson"
    print ()
if answer == 4:
    print ("Oh, so you are a Low T Beta then? Maybe that girl will touch you some day")
    baseINT=3
    baseCHAR=1
    baseSTR=1
    baseDNG=0
    race="Beta Faggot"
    print ()
AP = 18
print ("Points Left: ", AP)
while INT < 1 or INT > 10:
    print("Pick intelligence(1 to 10). Intelligence determines how you can persuade, and how quickly you level")
    while True:
        try:
            INT = input()
            INT = int(INT)
            break
        except ValueError:
            print("Enter an integer cocksucker")
AP = AP - INT
print ("Points Left: ", AP)
print ()
if AP < 11:
    while STR < 1 or STR > (AP-2):
        print ("Pick strength (1 to",AP-2,"). Strength contributes to total health and damage.")
        while True:
            try:
                STR = input()
                STR = int(STR)
                break
            except ValueError:
                print("Enter an integer cocksucker")        
if AP > 10:
    while STR < 1 or STR > 10:
        print("Pick strength(1 to 10). Strength contributes to total health and damage.")
        while True:
            try:
                STR = input()
                STR = int(STR)
                break
            except ValueError:
                print("Enter an integer cocksucker") 
AP = AP - STR
print ("Points Left: ", AP)
print ()
if AP < 11:
    while DNG < 1 or DNG > (AP-1):
        print ("Pick DONG (1 to",AP-1,")")
        while True:
            try:
                DNG = input()
                DNG = int(DNG)
                break
            except ValueError:
                print("Enter an integer cocksucker") 
if AP > 10:
    while DNG < 1 or DNG > 10:
        print("Pick DONG(1 to 10)")
        while True:
            try:
                DNG = input()
                DNG = int(DNG)
                break
            except ValueError:
                print("Enter an integer cocksucker")
AP = AP - DNG
print ("Points Left: ", AP)
print ()
if AP < 10:
    while CHAR < 1 or CHAR > AP:
        print ("Pick CHAR (1 to",AP,")")
        while True:
            try:
                CHAR = input()
                CHAR = int(CHAR)
                break
            except ValueError:
                print("Enter an integer cocksucker") 
if AP > 9:
    while CHAR < 1 or CHAR > 10:
        print("Pick CHAR(1 to 10)")
        while True:
            try:
                CHAR = input()
                CHAR = int(CHAR)
                break
            except ValueError:
                print("Enter an integer cocksucker")
AP = AP - CHAR
INT=INT+baseINT
STR=STR+baseSTR
DNG=DNG+baseDNG
CHAR=CHAR+baseCHAR
cialis = 0
ritalin = 0
health = 9 * STR + math.floor(DNG/2)+math.floor(CHAR/2)+20
hp = health
dong = DNG
exp = 0
loans=1
playerstats()
#chapter 1
print()
print("On the way to town, you are stopped by a drifter seeking assistance")
print("1. Okay")
askme()
print("Drifter: Ah, my lucky day, I did not think I would pass anyone else out here, my cart has broken down just off the road over there, could you help me gather up some supplies and escort me into town, I will pay you well for this")
answer=0
while answer >2 or answer<1:
    print("1. I will help you, drifter")
    print("2. Make the journey to town without my help")
    askme()
if answer==2:
    print("Drifter: fine, then I will pave the way with your blood!")
    print()
    racewar(98,1)
    print("You defeat the drifter and make it the rest of the way to town without incident")
    print()
    answer=0
if answer==1:
    print("You follow the drifter to the broken waggon, upon inspection of the wagon, it appears to be functional")
    answer=0
    while answer >2 or answer<1:
        print("1. Attack drifter")
        print("2. help the drifter")
        askme()
    if answer==1:
        print("You begin an unwarranted attack on the drifter")
        racewar(98,1)
        answer=1
    if answer==2:
        if race=="Meatperson":
            print("You assist the drifter and make it the rest of the way to town without incident")
            print("......")
            print("Thank you for your assistance, us Meatpersons need to stick together, this land is not kind to us. please, take this gold")
            loans=loans+50
        if race != "Meatperson":
            print("The drifter turns on you and attacks")
            racewar(98,1)
            print("You defeat the drifter and make it the rest of the way to town without incident")
            print()
def innatown():
        global hp
        global health
        global dong
        global dng
        global cialis
        global ritalin
        global level
        global STR
        global INT
        global DNG
        global exp
        global loans
        global gun
        global doggo
        global answer
        global weapon
        global ATK
        global swipes
        global CHAR
        global race
        global biome
        global armor
        global fame
        global infamy
        answer = 0
        while answer > 5 or answer < 1:
            print ("What to do?")
            print ("1. Visit Merchant")
            print ("2. Visit tavern")
            print ("3. Visit Meatperson Temple")
            print ("4. Go to town square to seek work")
            print ("5. Investigate Alley")
            askme()
            if answer == 1:
                    beanman()
                    answer = 0
            if answer == 2:
                    print ("You visit your favorite tavern, the ROGERS MUFF GARDEN, and take a seat.")
                    answer = 0
                    while answer > 4 or answer < 1:
                        print ("What to do?")
                        print ("1. [2 Gold] Order drink")
                        print ("2. Confront bar patron")
                        print ("3. *Show DONG* and leave")
                        print ("4. Compete in drinking competition")
                        askme()
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
                        print ("Bar Patron: What did you say about my mother?!")
                        answer = 0
                        while answer > 3 or answer < 1:
                            print ("1. Fight me, asshat")
                            if INT > 4:
                                print ("2. [INT] You seem to forget, you owe me some coin")
                            if INT < 5:
                                print ("2. [INT] She was less fat than the average woman of her age")
                            print ("3. *Show DONG*")
                            askme()
                            if answer ==1:
                                racewar (5,1)
                                print(" You win the brawl and leave the bar")
                                hp = health
                                dong = DNG
                            if answer == 2:
                                if INT < 5:
                                    print ("You trip and are mugged and lose some gold, you leave in embarassment")
                                    loans = loans-20
                                    if loans <0:
                                        loans=0
                                if INT > 4:
                                    trickchance=random.randrange(1,4,1)
                                    if trickchance>2:
                                        print ("Bar Patron: Oh, right, here you go")
                                        loans=loans+2
                                    if trickchance<3:
                                        print ("Bar Patron: Nice try, c'mere ya cunt")
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
                    if answer == 4:
                        if gun ==0:
                            if DNG > 0:
                                    print ("Bar Tender: Today only, we are having a drinking competition. The rules are simple: Drink beer without puking, and face trivia and challenges allong the way. The reigning champ was Nigerius Liberius, who made it to round 6. Beat that, and you will receive a prize")
                                    drinkingcomp()
                    answer = 0
            if answer == 3:
                print ("TEXT HERE")
                answer = 0
            if answer == 4:
                questbuilder()
                answer = 0
            if answer == 5:
                print ("TEXT HERE")
                answer = 0
innatown()
    

