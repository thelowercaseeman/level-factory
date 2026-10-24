import time
import random
import os


os.system('cls' if os.name == 'nt' else 'clear') # clears console


# vars
exitquestion = False
level = 0
rocupgrades = 0
stillplaying = True
stillshop = True
rocupgradesleft = 2





#minigames

def rockpaperscissors(ezness): # DONE
    global level
    global stillplaying
    os.system('cls' if os.name == 'nt' else 'clear')
    if ezness == 0:
        rockpaperscissorsnpc = random.randint(1,3)
        print("You are playing rock paper scissors. 1 = rock, 2 = paper, 3 = scissors, 4 = go back.")
        rockpaperscissorsplayed = input("")
        if rockpaperscissorsplayed == "1" or rockpaperscissorsplayed == "2" or rockpaperscissorsplayed == "3":
            if rockpaperscissorsnpc == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU LOSE")
                time.sleep(0.4)
            elif rockpaperscissorsnpc == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU TIE")
                time.sleep(0.4)
            elif rockpaperscissorsnpc == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU WIN")
                level += 1
                time.sleep(0.4)
        elif rockpaperscissorsplayed == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)
    elif ezness == 1:
        rockpaperscissorsnpc = random.randint(1,6)
        print("You are playing rock paper scissors. 1 = rock, 2 = paper, 3 = scissors, 4 = go back.")
        rockpaperscissorsplayed = input("")
        if rockpaperscissorsplayed == "1" or rockpaperscissorsplayed == "2" or rockpaperscissorsplayed == "3":
            if rockpaperscissorsnpc == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU LOSE")
                time.sleep(0.4)
            elif rockpaperscissorsnpc == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU TIE")
                time.sleep(0.4)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU WIN")
                level += 1
                time.sleep(0.4)
        elif rockpaperscissorsplayed == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)
    elif ezness == 2:
        print("You are playing rock paper scissors. 1 = rock, 2 = paper, 3 = scissors, 4 = go back.")
        rockpaperscissorsplayed = input("")
        if rockpaperscissorsplayed == "1" or rockpaperscissorsplayed == "2" or rockpaperscissorsplayed == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("YOU WIN")
            time.sleep(0.4)
        elif rockpaperscissorsplayed == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)


# the game
while exitquestion == False:
    rocupgradesleft = int(rocupgradesleft)
    rocupgradesleft = 2 - rocupgrades
    rocupgradesleft = str(rocupgradesleft)
    stillplaying = True
    stillshop = True
    os.system('cls' if os.name == 'nt' else 'clear')
    print("LEVEL:")
    print(level)
    print("__")
    print("||")
    print("||")
    print("||")
    print("||      __     __     __     __       ")
    print("||______||_____||_____||_____||_____")
    print("| Welcome to the Level Factory!")
    print("|")
    print("| Your goal is to reach the highest level you can.")
    print("| Commands:")
    print("| 1 = shop, 2 = rock paper scissors, 'esc' is exit.")
    print("|")
    levelfactorycommands = input("")
    if levelfactorycommands == "1": # DONE
        while stillshop == True:
            rocupgradesleft = int(rocupgradesleft)
            rocupgradesleft = 2 - rocupgrades
            rocupgradesleft = str(rocupgradesleft)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("LEVEL:")
            print(level)
            print("__")
            print("||")
            print("||")
            print("||")
            print("||      __     __     __     __       ")
            print("||______||_____||_____||_____||_____")
            print("| Welcome to the Level Factory Shop!")
            print("|")
            print("| Here, you can upgrade your factory to get more levels by spending levels!")
            print("| Commands:")
            print("| 0 = return, 1 = upgrade rock paper scissors for 5 levels (" + rocupgradesleft + " UPGRADE(S) LEFT),")
            print("|")
            rocupgradesleft = int(rocupgradesleft)
            shopinput = input("")
            if shopinput == "0": # DONE
                stillshop = False
            elif shopinput == "1": # DONE
                if rocupgradesleft == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("YOU HAVE MAXED THAT UPGRADE")
                    time.sleep(1)
                elif level >= 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Rock paper scissors has now been upgraded!")
                    rocupgrades += 1
                    level = level - 5
                    time.sleep(1)
                elif level < 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("You do not have enough levels to upgrade that.")
                    time.sleep(1)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("NOT AN OPTION")
                time.sleep(1)
    elif levelfactorycommands == "2": # DONE
        while stillplaying == True:
            rockpaperscissors(rocupgrades)
    elif levelfactorycommands == "esc": # DONE
        exitquestion = True
        os.system('cls' if os.name == 'nt' else 'clear')
    else: # DONE
        os.system('cls' if os.name == 'nt' else 'clear')
        print("NOT AN OPTION")
        time.sleep(1)
