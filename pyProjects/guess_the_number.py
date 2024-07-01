import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
comChoice = random.choice(nums)
# print(comChoice)
print("You are entering to the GTN game [developed by rh]")
play = input("Hit enter to continue...")
while play != "":
    play = input("Please hit enter to continue...")
else:
    usrChoice = int(input("Enter the number: "))
    while usrChoice != comChoice:
        
        print("Upps! Number doesn't match.")
        hint = input("Do you want a hint?(yes/no): ")
        if hint == "yes":
            if comChoice - usrChoice == 3 or comChoice - usrChoice == 2 or comChoice - usrChoice == 1:
                print("You are too close!")
            elif comChoice - usrChoice == -3 or comChoice - usrChoice == -2 or comChoice - usrChoice == -1 :
                print("You are too close!")
            else:
                print("You are far from the ans. Try Harder!")
        
        usrChoice = int(input("Enter the number: "))
    else:
        print("yeyeee! You got me Brilliant!")

            


    

    
