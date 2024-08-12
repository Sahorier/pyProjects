import os
import sys

def clear():
    # Check if the system is Windows      (clear function Taken from pieces)
    if os.name == 'nt':
        os.system('cls')
    # For Unix-based systems
    else:
        os.system('clear')

def answers(x):
    global balance
    global ques
    again1 = "yes"
    chance = 0
    while again1.lower() == "yes":
        chance = chance + 1
        if chance <= 3:
            if chance == 3:
                print("It is your last Chance. Be Careful!")
            print("Your balance is now BDT", balance)
            print(ques[x][0])
            ans0 = input("Ans: ")
            ans0 = ans0.title()
            if ( ans0 == ques[x][1]):
                
                print("Congratulations!",name , "You won BDT", balance)
                balance = balance + balance
                print("Your balance is now BDT", balance)
                again1 = "no"
                clear()
            else:
                if chance <= 2:
                    print("Wrong Answer!")
                    balance = balance * (2/3)
                    print("Your balance is now BDT", balance)
                    if chance == 2:
                        print("It will be your last chance. Be careful!")
                    again1 = input("Do you want to try again? (yes/no): ")
                    clear()
                    
                else:
                    continue
        else:
            print("Sorry, you've lost!")
            print("Better luck next time.")
            sys.exit()   # sys module taken from pieces

def fanswers(x):
    global balance
    global fques
    print("Your balance is now BDT",balance)
    print(fques[x][0])
    fans = input("Ans: ")
    fans = fans.title()
    if ( fans == fques[x][1]):
        print("Congratulations!",name , "You won BDT", balance)
        balance = balance + (balance * (1/2))
        clear()
    elif ( fans == "Skip"):
        clear()
        pass
    else:
        print("Wrong Answer!")
        print("Sorry! You've lost.")
        balance = 00
        print("Your balance is now BDT", balance)
        sys.exit()   # sys module taken from pieces

name = input("Enter your name: ")
name = name.title()
balance = int(input("Amount to diposit: "))
ques = [["What is your name?",name],["In which year Bangladesh got the real victory?","2024"],["What comes after 5?", "6"],[],]
answers(0)
answers(1)
answers(2)
print("Be carefull! You are entering the finals.")
print("Now there will no extra chances. You can write \"skip\" to skip the questions.")
print("A wrong answer will empty your balance!")
finals = input("Do you want to continue?(yes/no): ")
fques = [["Who is the New Chief Minister of bangladesh?","Dr Muhammad Yunus"],["Who is the 1st martyr of 2024 Quota movement?", "Abu Sayed"],["\"Chatro league er chamra\", Complete the sentance:", "Tule Dibo Amra"]]
if finals == "yes":
    fanswers(0)
    fanswers(1)
    fanswers(2)
    print("You've won BDT",balance,"! Now give the programme owner BDT",balance,"XD")
else:
    print("You've lost all your money. You can't withdrow it without playing the finals.")
print("Under development! (Bugs are available)")