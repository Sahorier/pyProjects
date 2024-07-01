import random

user_action = input("Enter a choice (rock, paper, scissor) : ")
possible_action = ["rock", "paper", "scissor"]
computer_action = random.choice(possible_action)
print(f"\nYou choose {user_action}, computer choose {computer_action}. \n")

if computer_action == user_action:
    print(f"You both choose {user_action}, Tie")
elif user_action == "rock":
    if computer_action == "scissor":
        print("Rock smashes Scissor, you win!")
    elif computer_action == "paper":
        print("Paper catches Rock, You loose!")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper catches Rock, You Win!")
    elif computer_action == "scissor":
        print("Scissor cuts Paper, You loose!")
elif user_action == "scissor":
    if computer_action == "paper":
        print("Scissor cuts Paper, You Win!")
    elif computer_action == "rock":
        print("Rock smashes Scissor, You loose!")
elif user_action == "rock.":  # Cheat code.
    print("Congratulations! you win")
elif user_action == "paper.":
    print("Congratulations! you win")
elif user_action == "scissor.":
    print("Congratulations! you win")

    # play_again = input("Play again? (y/n): ")
    # if play_again.lower() != "y":
    #      break
