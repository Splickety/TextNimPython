
from random import randint

size_setting = 10
size = 10
removable = 3
ai_perfect = True
ai_first = False
last_token_loses = True

def take(x):
    global size
    size = size - x

def takeAI():
    ai_take = 1
    if ai_perfect == False and size > removable:
        ai_take = randint(1,removable)
    else:
        mod = size%(removable + 1)
        if last_token_loses == True:
            if mod == 1:
                ai_take = 1
            elif mod == 0:
                ai_take = removable
            else:
                ai_take = mod - 1
        else:
            if mod == 0:
                ai_take = 1
            else:
                ai_take = mod
    take(ai_take)
    print("AI takes: " + str(ai_take))


def askForTake():
    response = input(rules())
    if not str.isdigit(response):
        print("That's not a valid input.")
        askForTake()
    elif  int(response) > removable or int(response) < 1:
        print("That digit is not within the range.")
        askForTake()
    else:
        take(int(response))



def rules():
    return str("How many would you like to take? Pick a number between 1 and " + str(removable) + " : ")


def printCurrentSettings():
    print("Size: " + str(size_setting))
    print("Removable: " + str(removable))
    print("Last Token Removed Loses: " + str(last_token_loses))
    print("AI plays perfectly: " + str(ai_perfect))
    print("AI goes first: " + str(ai_first))

def modifySettings():
    print("---MODIFYING SETTINGS---")
    modifySize()
    modifyRemovable()
    global last_token_loses
    last_token_loses = modifyTrueFalse("Last token loses")
    global ai_perfect 
    ai_perfect = modifyTrueFalse("AI plays perfectly")
    global ai_first
    ai_first = modifyTrueFalse("AI goes first")
    print("---UPDATED SETTINGS---")
    printCurrentSettings()
    mainMenu()

def modifyTrueFalse(name):
    response = input(name + ", (t)rue or (f)alse: ")
    if not (response == "t" or response == "f"):
        print("Response must be t or f, lowercase.")
        modifyTrueFalse(name)
    elif response == "t":
        return True
    else:
        return False

def modifyRemovable():
    removable_input = input("Removable: ")
    if not str.isdigit(removable_input):
        print("Response must be an integer.")
        modifySize()
    elif int(removable_input) >= size_setting:
        print("Response must be less than the size of the game, which is " + str(size_setting))
        modifySize()
    else:
        global removable
        removable = int(removable_input)


def modifySize():
    size_input = input("Size: ")
    if not str.isdigit(size_input):
        print("Response must be an integer.")
        modifySize()
    elif int(size_input) < 3:
        print("Response must be greater than 2.")
        modifySize()
    else:
        global size_setting
        size_setting = int(size_input)

def mainMenu():
    print("---MAIN MENU---")
    print("Welcome to the legendary game of Nim")
    print("(p)lay game")
    print("(s)ettings")
    print("(q)uit")
    menu_choice = input("p, s, or q? : ")
    while not (menu_choice == "p" or menu_choice == "s" or menu_choice == "q"):
        print("Response must be p, s or q, lowercase.")
        menu_choice = input("p, s, or q? : ")
    if menu_choice == "p":
        play()
    elif menu_choice == "s":
        settings()
    else:
        print("Now quitting program. Goodbye!")
        quit

def play():
    print("---PLAY GAME---")
    global size
    size = size_setting
    if ai_first:
        aiTurn()
    else:
        playerTurn()

def playerTurn():
    print("Remaining: " + str(size))
    askForTake()
    if size <=0:
        playerEnd()
    else:
        aiTurn()
def aiTurn():
    print("Remaining: " + str(size))
    takeAI()
    if size <=0:
        aiEnd()
    else:
        playerTurn()

def playerEnd():
    print("You took the last piece.")
    if last_token_loses:
        print("You lose. :/")
    else:
        print("You win!!!")
    print("---GAME OVER---")
    print("Returning to Menu")
    mainMenu()

def aiEnd():
    print("The ai took the last piece.")
    if last_token_loses:
        print("You win!!!")
    else:
        print("You lose. :/")
    print("---GAME OVER---")
    print("Returning to Menu")
    mainMenu()


def settings():
    print("---SETTINGS---")
    printCurrentSettings()
    print("Would you like to modify?")
    yes_or_no = input("(y)es or (n)o? : ")
    while not (yes_or_no == "y" or "n"):
        print("That is not a valid input. Type y or n, lowercase.")
        yes_or_no = input("p, s, or q? : ")
    if yes_or_no == "y":
        modifySettings()
    else:
        mainMenu()




#Main Program
mainMenu()
