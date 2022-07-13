import cv2
from keras.models import load_model
import numpy as np
import random
import time

from pip import main


class RPS:
    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.countdown_timer = 5
        self.user_wins = 0
        self.computer_wins = 0
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.start_time = time.time
        self.rounds = 1

    #start camera video input
    def start_video(self):
        while True:                       
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)

            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    #Timer after start video
    #Countdown Timer
    def start_timer(self):
        while countdown_timer:
            self.countdown_timer = 5
            mins, secs = divmod(countdown_timer,60)
            timer = '{02d}:{02d}'.format(mins, secs)
            print (timer, end="\r")
            time.sleep(1)
            countdown_timer -= 1
        print ('Show your hand - Rock, Paper or Scissors?')
        
    #game_timer function call 'start_timer(int(coundown_timer))'


    # User input from Camera
    def get_prediction(self):
        prediction = self.model.predict(self.data)
        max_probability = np.argmax(prediction[0])
        return max_probability

    #Game functions
    def get_computer_choice(self):
        print(self.computer_choice)

    def get_user_choice(self):
        print(self.get_prediction)
        
    def get_winner(self):
        if self.get_user_choice == self.computer_choice:
            print(f"Both players selected {self.get_user_choice}. It's a tie!")
        elif self.get_user_choice == "Rock":
            if self.computer_choice == "Scissors":
                self.user_wins = self.user_wins+1
                print ("Rock beats Scissors! You win!")
            else:
                self.computer_wins = self.computer_wins+1
                print ("Paper covers Rock! You lose.")
        elif self.get_user_choice == "Paper":
            if self.computer_choice == "Rock":
                self.user_wins = self.user_wins+1
                print("Paper covers Rock! You win!")
            else:
                self.computer_wins = self.computer_wins+1
                print("Scissors cuts Paper! You lose.")
        elif self.get_user_choice == "Scissors":
            if self.computer_choice == "Paper":
                self.user_wins = self.user_wins+1
                print("Scissors cuts paper! You win!")
            else:
                self.computer_wins = self.computer_wins+1
                print("Rock beats Scissors! You lose.")
    
    def stop_video(self):
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    def play_timer(self):
        self.start_timer(self.countdown_timer)
    def play_again (self):
        self.rounds = 1
        while self.rounds<5:
            print (f"Start round {self.rounds}")
            if self.user_wins < 3 and self.computer_wins < 3:
                self.play_timer
                self.start_video
                self.get_user_choice
                self.get_computer_choice
                self.get_winner            
            elif self.user_wins == 3 and self.computer_wins < self.user_wins:
                print ("You Win the Game, Goodbye")
                self.stop_video
            elif self.computer_wins == 3 and self.user_wins < self.computer_wins:
                print ("I Win the Game, You Lose! Goodbye")
                self.stop_video
            else:
                print ("GAME OVER")
                self.stop_video
            self.rounds+=1
        return

if __name__ == '__main__':
    main()


    
            