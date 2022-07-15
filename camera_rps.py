import cv2
from keras.models import load_model
import numpy as np
import random
import time


class RPS:
    def __init__(self):        
        self.user_wins = 0
        self.computer_wins = 0
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])        
        self.end_time = time.time() + 5
        self.t = self.end_time - time.time()
        self.rounds = 1

    #start camera video input
    def start_video(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)        
        while time.time < self.end_time:                                
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            self.prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            print(self.prediction)
            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    #Timer after start video
    #Countdown Timer
    def start_timer(self):  
        # time.time()      
        while time.time < self.end_time:
            print (self.t)
            t += 1            
        print ('Show your hand - Rock, Paper or Scissors?')
        
    #game_timer function call 'start_timer(int(coundown_timer))'

    # User input from Camera
    def get_prediction(self):
        self.start_video()
        self.prediction = self.model.predict(self.data)
        self.max_probability = np.argmax(self.prediction[0])
        print(self.max_probability)
        return self.max_probability

    #Game functions
    def get_computer_choice(self):
        print(self.computer_choice)

    def get_user_choice(self):
        self.get_prediction()
        if self.max_probability == 0:            
            print("Rock")
            return "Rock"
        elif self.max_probability == 1:            
            print("Paper")
            return "Paper"
        elif self.max_probability == 2:            
            print("Scissors")
            return "Scissors"
        else:
            print("Nothing")
            return "Nothing"  

        
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
    
    def start_game(self):
        self.get_user_choice()
        self.get_computer_choice()
        self.get_winner()

    
    def stop_video(self):
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    
def play():
    rps = RPS()
    rps.rounds = 1
    while rps.rounds<6:
        print (f"Start round {rps.rounds}")
        if rps.user_wins < 3 and rps.computer_wins < 3:
            rps.start_timer
            rps.start_video
            rps.start_game            
        elif rps.user_wins == 3 and rps.computer_wins < rps.user_wins:
            print ("You Win the Game, Goodbye")
            rps.stop_video
        elif rps.computer_wins == 3 and rps.user_wins < rps.computer_wins:
            print ("I Win the Game, You Lose! Goodbye")
            rps.stop_video
        else:
            print ("GAME OVER")
            rps.stop_video
        rps.rounds+=1
    
play()
