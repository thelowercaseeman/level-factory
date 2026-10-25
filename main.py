import base64


your_code = base64.b64encode(b"""







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
levelmultiplier = 1
mindreaderupgrades = 0
mindreaderupgradesleft = 3



# minigames

def rockpaperscissors(ezness): # DONE
    global levelmultiplier
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
                level = level + (1 * levelmultiplier)
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
                level = level + (1 * levelmultiplier)
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
            level = level + (1 * levelmultiplier)
            print("YOU WIN")
            time.sleep(0.4)
        elif rockpaperscissorsplayed == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)


def mindreader(ezness): # DONE
    global levelmultiplier
    global level
    global stillplaying
    os.system('cls' if os.name == 'nt' else 'clear')
    if ezness == 0: 
        print("Guess a number 1 through ten, 'esc' = exit.")
        mindreaderinput = input("")
        if mindreaderinput == "1" or mindreaderinput == "2" or mindreaderinput == "3" or mindreaderinput == "4" or mindreaderinput == "5" or mindreaderinput == "6" or mindreaderinput == "7" or mindreaderinput == "8" or mindreaderinput == "9" or mindreaderinput == "10":
            mindreadernpc = random.randint(1,25)
            if mindreadernpc == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED CORRECTLY")
                level = level + (20 * levelmultiplier)
                time.sleep(0.4)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED INCORRECTLY")
                time.sleep(0.4)
        elif mindreaderinput == "esc":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)
    if ezness == 1:
        print("Guess a number 1 through ten, 'esc' = exit.")
        mindreaderinput = input("")
        if mindreaderinput == "1" or mindreaderinput == "2" or mindreaderinput == "3" or mindreaderinput == "4" or mindreaderinput == "5" or mindreaderinput == "6" or mindreaderinput == "7" or mindreaderinput == "8" or mindreaderinput == "9" or mindreaderinput == "10":
            mindreadernpc = random.randint(1,10)
            if mindreadernpc == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED CORRECTLY")
                level = level + (20 * levelmultiplier)
                time.sleep(0.4)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED INCORRECTLY")
                time.sleep(0.4)
        elif mindreaderinput == "esc":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)
    if ezness == 2:
        print("Guess a number 1 through ten, 'esc' = exit.")
        mindreaderinput = input("")
        if mindreaderinput == "1" or mindreaderinput == "2" or mindreaderinput == "3" or mindreaderinput == "4" or mindreaderinput == "5" or mindreaderinput == "6" or mindreaderinput == "7" or mindreaderinput == "8" or mindreaderinput == "9" or mindreaderinput == "10":
            mindreadernpc = random.randint(1,5)
            if mindreadernpc == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED CORRECTLY")
                level = level + (20 * levelmultiplier)
                time.sleep(0.4)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED INCORRECTLY")
                time.sleep(0.4)
        elif mindreaderinput == "esc":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)
    if ezness == 3:
        print("Guess a number 1 through ten, 'esc' = exit.")
        mindreaderinput = input("")
        if mindreaderinput == "1" or mindreaderinput == "2" or mindreaderinput == "3" or mindreaderinput == "4" or mindreaderinput == "5" or mindreaderinput == "6" or mindreaderinput == "7" or mindreaderinput == "8" or mindreaderinput == "9" or mindreaderinput == "10":
            mindreadernpc = random.randint(1,2)
            if mindreadernpc == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED CORRECTLY")
                level = level + (20 * levelmultiplier)
                time.sleep(0.4)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED INCORRECTLY")
                time.sleep(0.4)
        elif mindreaderinput == "esc":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)
    if ezness == 4:
        print("Guess a number 1 through ten, 'esc' = exit.")
        mindreaderinput = input("")
        if mindreaderinput == "1" or mindreaderinput == "2" or mindreaderinput == "3" or mindreaderinput == "4" or mindreaderinput == "5" or mindreaderinput == "6" or mindreaderinput == "7" or mindreaderinput == "8" or mindreaderinput == "9" or mindreaderinput == "10":
            mindreadernpc = random.randint(1,1)
            if mindreadernpc == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED CORRECTLY")
                level = level + (20 * levelmultiplier)
                time.sleep(0.4)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("YOU GUESSED INCORRECTLY")
                time.sleep(0.4)
        elif mindreaderinput == "esc":
            os.system('cls' if os.name == 'nt' else 'clear')
            stillplaying = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)


# other stuff

def superrebirth(amount): # DONE
    global levelmultiplier
    global rocupgrades
    global level
    global mindreaderupgrades
    if amount > 1000000000000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 100000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 100000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 10000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 10000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(1)
    elif amount > 1000000:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You have successfully rebirthed!")
        levelmultiplier = levelmultiplier * 1000
        level = 0
        rocupgrades = 0
        mindreaderupgrades = 0
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
    print("| 1 = shop, 2 = rock paper scissors, 3 = mind reader, 4 = achievements, 0 = enter rebirth shop, 'esc' = exit.")
    print("|")
    levelfactorycommands = input("")
    if levelfactorycommands == "1": # DONE
        while stillshop == True:
            rocupgradesleft = int(rocupgradesleft)
            rocupgradesleft = 2 - rocupgrades
            rocupgradesleft = str(rocupgradesleft)
            mindreaderupgradesleft = int(mindreaderupgradesleft)
            mindreaderupgradesleft = 4 - mindreaderupgrades
            mindreaderupgradesleft = str(mindreaderupgradesleft)
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
            print("| 0 = return, 1 = upgrade rock paper scissors for 10 levels (" + rocupgradesleft + " UPGRADE(S) LEFT), 2 = upgrade mind reader for 150 levels (" + mindreaderupgradesleft + " UPGRADE(S) LEFT")
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
                elif level >= 10:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Rock paper scissors has now been upgraded!")
                    rocupgrades += 1
                    level = level - 10
                    time.sleep(1)
                elif level < 10:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("You do not have enough levels to upgrade that.")
                    time.sleep(1)
            elif shopinput == "2": # DONE
                if mindreaderupgradesleft == "0":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("YOU HAVE MAXED THAT UPGRADE")
                    time.sleep(1)
                elif level < 150:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("You do not have enough levels to upgrade that.")
                    time.sleep(1)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Mind reader has now been upgraded!")
                    mindreaderupgrades += 1
                    level = level - 150
                    time.sleep(1)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("NOT AN OPTION")
                time.sleep(1)
    elif levelfactorycommands == "2": # DONE
        while stillplaying == True:
            rockpaperscissors(rocupgrades)
    elif levelfactorycommands == "3": # DONE
        while stillplaying == True:
            mindreader(mindreaderupgrades)
    elif levelfactorycommands == "4":
        while stillshop == True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Welcome to the achievements page! This also functions as a statistics page.")
            print("Level: " + str(level))
            print("Level multiplier: " + str(levelmultiplier))
            print("I'm lying, I'm too lazy to actually add achievements.")
            print("0 = go back to main menu")
            achievementpageexit = input("")
            if achievementpageexit == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                stillshop = False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("NOT AN OPTION")
                time.sleep(1)
    elif levelfactorycommands == "67" or levelfactorycommands == "six seven":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You think you're so funny, don't you?")
        time.sleep(3)
        print("Say goodbye to EVERYTHING.")
        level = 0
        levelmultiplier = 0
        rocupgrades = 0
        mindreaderupgrades = 0
        time.sleep(2)
        print("Hope that was worth it! :D")
        time.sleep(60)
        print("Just kidding! Hah, you waited a minute and the code is going to CLOSE ANYWAY. Goodbye!")
        exitquestion = True
    elif levelfactorycommands == "0": # DONE
        os.system('cls' if os.name == 'nt' else 'clear')
        print("LEVEL:")
        print(level)
        print("__")
        print("||")
        print("||")
        print("||")
        print("||      __     __     __     __       ")
        print("||______||_____||_____||_____||_____")
        print("| Welcome to the Level Factory Rebirth Shop!")
        print("|")
        print("| Here, you can add multipliers to your level gain! At a price, of course. Commands:")
        print("| 0 = return, 1 = assuming you have all rock paper scissors upgrades, spend all of your levels (at least 100) and wipe your upgrades to double your level gain!")
        print("| 2 = assuming you have all upgrades, spend all of your levels (at least 1000) to 10x your level gain!")
        print("| 3 = assuming you have all upgrades, spend a minimum of 1000000 levels to increase your level gain, depending on how many levels you have!")
        rebirthshopinput = input("")
        if rebirthshopinput == "0":
            stillshop = False
        elif rebirthshopinput == "1":
            if rocupgrades < 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You do not have all of the rock paper scissors upgrades.")
                time.sleep(1)
            elif level < 50:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You do not have enough levels.")
                time.sleep(1)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You have successfully rebirthed!")
                levelmultiplier = levelmultiplier * 2
                level = 0
                rocupgrades = 0
                mindreaderupgrades = 0
                time.sleep(1)
        elif rebirthshopinput == "2":
            if rocupgrades < 2 or mindreaderupgrades < 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You do not have all of the upgrades.")
                time.sleep(1)
            elif level < 1000:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You do not have enough levels.")
                time.sleep(1)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You have successfully rebirthed!")
                levelmultiplier = levelmultiplier * 10
                level = 0
                rocupgrades = 0
                mindreaderupgrades = 0
                time.sleep(1)
        elif rebirthshopinput == "3":
            if rocupgrades < 2 or mindreaderupgrades < 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You do not have all of the upgrades.")
                time.sleep(1)
            elif level < 1000000:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You do not have enough levels.")
                time.sleep(1)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You have successfully rebirthed!")
                superrebirth(level)
                time.sleep(1)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("NOT AN OPTION")
            time.sleep(1)
    elif levelfactorycommands == "esc": # DONE
        exitquestion = True
        os.system('cls' if os.name == 'nt' else 'clear')
    else: # DONE
        os.system('cls' if os.name == 'nt' else 'clear')
        print("NOT AN OPTION")
        time.sleep(1)






""")



exec(base64.b64decode(your_code))
