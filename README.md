# CV-Rock-Paper-Scissors
## Project 1 - Computer Vision Rock Paper Scissors

### Milestone 1

Used Teachablemachine.com to create a model for image input of the game Rock-Paper-Scissors. The model has classes - Rock, Paper, Scissors and 'Nothing'.  I then downloaded the trained model. This model will be used to get the user input for the game.

### Installed Dependencies

The following libraries were installed to facilitate running the trained model. A new environment for the game was created in the Conda environment and the following libraries installed in it: pip, opencv-python, tensorflow, and ipykernel.
The trained model files are saved in the project folder as keras.model.h5 and labels.txt to run model on local machine using the code in the model.py file.

### Manual Rock-Paper-Scissors game

First, a manual Rock-Paper-Scissors file with code to take user input typed-in, playing with the computer with output of the winner was created in the manual.rps.py file. This code takes in and stores the user's input using the function "get_user_choice" and then uses the 'random' module to create and store the computer's choice using the function "get_computer_choice". the "get_winnner" function then compares the computer_choice to the user_choice to determin the winner of the game. Finally the "play" function calls the three functions (get_computer_choice, get_user_choice, and get_winner) to simulate the game.

### Complete Game

#### Modules Used

Imported modules include cv2, load_model from keras.models, numpy, random and time.

The cv2, load_model from keras.models and numpy modules are used to start the camera for video input of user choice.

The random module used for the random selection of computer choice during the game
And the time module for the timers

#### Functionality

The game consists of five (5) components;

##### Component 1: Countdown timer to start game

When the game is run, it starts with a countdown timer from 5 seconds to 0 at which computer prompts the user for their choice in the game and at the same time the computer randomly selects a choice. These two choices are combined into one class so that both choices (computer and user) are made at the same time

##### Component 2: Video User Input and Trained Model

At the end of the 5 second timer, the camera is started to obtain the user video input. The module that captures and interprets the user input was created using 'Teachablemachine.com' with multiple images of the choices --> Rock, Paper, Scissors and Nothing. And then downloaded in keras format. It is then imported into the game code using load_model from keras_models.

##### Component 3: Random Generation of Computer choice

The 'random' module was imported to facilitate the computer to make a random selection from the 3 choices --> Rock, Paper, or Scissor

##### Component 4: Wins and Losses

The get_winner function uses the if-else methodology to compare the user and computer input choices to determine the winner. It then keeps count of the number of wins. The ultimate winner is the one who gets to 3 wins first.

##### Component 5: End Game

The game is ended in one of 3 ways; upon getting to the ultimate winner, or after 6 rounds, or ended by the user by pressing q for Quit.
