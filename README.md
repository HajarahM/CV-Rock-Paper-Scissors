# CV-Rock-Paper-Scissors
Project 1 - Computer Vision Rock Paper Scissors

Milestone 1 - Used Teachablemachine.com to create a model for image input of the game Rock-Paper-Scissors. The model has classes - Rock, Paper, Scissors and 'Nothing'.  I then downloaded the trained model. This model will be used to get the user input for the game.

Installed Dependencies
The following libraries were installed to facilitate running the trained model. A new environment for the game was created in the Conda environment and the following libraries installed in it: pip, opencv-python, tensorflow, and ipykernel.
The trained model files are saved in the project folder as keras.model.h5 and labels.txt to run model on local machine using the code in the model.py file.

Manual Rock-Paper-Scissors game
First, a manual Rock-Paper-Scissors file with code to take user input typed-in, playing with the computer with output of the winner was created in the manual.rps.py file. This code takes in and stores the user's input using the function "get_user_choice" and then uses the 'random' module to create and store the computer's choice using the function "get_computer_choice". the "get_winnner" function then compares the computer_choice to the user_choice to determin the winner of the game. Finally the "play" function calls the three functions (get_computer_choice, get_user_choice, and get_winner) to simulate the game.