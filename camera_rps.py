import cv2
from keras.models import load_model
import numpy as np
import random
import time


#Definitions for Camera User Input 
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
countdown_timer = 5
user_wins = 0
computer_wins = 0
# Choices
action_choice = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(action_choice)

#start camera video input
def start_video ():
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_video()

#Timer after start video
#Countdown Timer
def start_timer():
    while countdown_timer:
        mins, secs = divmod(countdown_timer,60)
        timer = '{02d}:{02d}'.format(mins, secs)
        print (timer, end="\r")
        time.sleep(1)
        countdown_timer -= 1
    print ('Show your hand - Rock, Paper or Scissors?')
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    get_prediction()
#game_timer function call 'start_timer(int(coundown_timer))'


# User input from Camera
def get_prediction():
    prediction = model.predict(data)
    max_probability = np.argmax(prediction[0])
    return max_probability

user_choice = get_prediction()

#Game functions
class GameChoices():
    def get_computer_choice ():
        print (computer_choice)
    def get_user_choice():
        user_choice = get_prediction()
        print (user_choice)
game_choices = GameChoices()

class GetWinner ():
    def get_winner ():
        if user_choice == computer_choice:
            print (f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "Rock":
            if computer_choice == "Scissors":
                user_wins = user_wins+1
                print ("Rock beats Scissors! You win!")
            else:
                computer_wins = computer_wins+1
                print ("Paper covers Rock! You lose.")
        elif user_choice == "Paper":
            if computer_choice == "Rock":
                user_wins = user_wins+1
                print("Paper covers Rock! You win!")
            else:
                computer_wins = computer_wins+1
                print("Scissors cuts Paper! You lose.")
        elif user_choice == "Scissors":
            if computer_choice == "Paper":
                user_wins = user_wins+1
                print("Scissors cuts paper! You win!")
            else:
                computer_wins = computer_wins+1
                print("Rock beats Scissors! You lose.")
winner = GetWinner()

def stop_video():
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

class LetsPlay ():
    def play_timer ():
        start_timer(int(countdown_timer))
    def play_again (play_timer):
        if user_wins < 3 and computer_wins < 3:
            start_video
            play_timer
            game_choices
            winner
        elif user_wins == 3 and computer_wins < user_wins:
            print ("You Win the Game, Goodbye")
            stop_video
        elif computer_wins == 3 and user_wins < computer_wins:
            print ("I Win the Game, Goodbye")
            stop_video
        else:
            print ("GAME OVER")
            stop_video

Play = LetsPlay ()

if __name__ == '__main__':
    LetsPlay()

Play

  
        