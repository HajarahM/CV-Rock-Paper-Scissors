import cv2
from keras.models import load_model
import numpy as np
import model
import random
import time

start_time = time.time()

# function to return output of trained model
while True:

    def get_prediction():
        if model.prediction [0][0] > 0.8:
            print('Rock')
        elif model.prediction [0][1] > 0.8:
            print('Paper')
        elif model.prediction [0][2] > 0.8:
            print('Scissors')
        else:
            print('Nothing')
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

action_choice = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(action_choice)
user_choice = get_prediction()

#Game functions
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

game_time = time.time() - start_time
def play ():
    if game_time == 5:
        print ("It's game time, enter your choice")
        get_computer_choice()
        get_user_choice ()
        print(f"\n Computer chose {computer_choice}, You chose {user_choice}.\n")
        get_winner ()
    else:
        print("Not yet time to play")

    return



 
        



