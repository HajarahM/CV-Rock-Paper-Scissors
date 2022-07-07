import cv2
from keras.models import load_model
import numpy as np
import random
import time

#Definitions for Camera User Input 
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
prediction = model.predict(data)

start_time = time.time()
# User input from Camera
class UserCameraInput():
    def get_prediction():
        while True:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            cv2.imshow('frame', frame)
            if prediction [0][0] > 0.6:
                print('Rock')
            elif prediction [0][1] > 0.6:
                print('Paper')
            elif prediction [0][2] > 0.6:
                print('Scissors')
            else:
                print('Nothing')
           
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
end_time = time.time()  

# Choices
action_choice = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(action_choice)
user_choice = UserCameraInput()

#Game functions
class GameChoices():
    def get_computer_choice ():
        computer_choice
    def get_user_choice ():
        user_choice
game_choices = GameChoices()

user_win = 0
computer_win = 0

class GetWinner ():
    def get_winner ():
        if user_choice == computer_choice:
            print (f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "Rock":
            if computer_choice == "Scissors":
                user_win = user_win+1
                print ("Rock beats Scissors! You win!")
            else:
                computer_win = computer_win+1
                print ("Paper covers Rock! You lose.")
        elif user_choice == "Paper":
            if computer_choice == "Rock":
                user_win = user_win+1
                print("Paper covers Rock! You win!")
            else:
                computer_win = computer_win+1
                print("Scissors cuts Paper! You lose.")
        elif user_choice == "Scissors":
            if computer_choice == "Paper":
                user_win = user_win+1
                print("Scissors cuts paper! You win!")
            else:
                computer_win = computer_win+1
                print("Rock beats Scissors! You lose.")
winner = GetWinner()

#counter
game_time = end_time - start_time

class LetsPlay():
    def play_timer ():
        if game_time == 5:
            print ("It's game time, enter your choice")
            game_choices
            print(f"\n Computer chose {computer_choice}, You chose {user_choice}.\n")
            winner
        else:
            print("Not yet time to play")

  
        