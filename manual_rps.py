import random

action_choice = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(action_choice)
user_choice = input("Enter a choice (Rock, Paper, Scissors): ")

def get_computer_choice ():
    computer_choice
def get_user_choice ():
    user_choice

def get_winner ():
    if user_choice == computer_choice:
        print (f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print ("Rock beats Scissors! You win!")
        else:
            print ("Paper covers Rock! You lose.")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock beats Scissors! You lose.")

def play ():
    get_computer_choice()
    get_user_choice ()
    print(f"\n Computer chose {computer_choice}, You chose {user_choice}.\n")
    get_winner ()

play()