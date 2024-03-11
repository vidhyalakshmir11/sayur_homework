
# Problem #1
# Play the game Rock Papar Scissors with the computer.
# Play it three times and best of three wins. 
# If you win, print your name in color (look for a python package to do this)
# Hint - Use random number generation
import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
       return "die"
    elif (user_choice == 'rock' and  computer_choice == 'paper') or (user_choice == 'paper' and  computer_choice == 'scissors') or (user_choice == 'scissors' and  computer_choice == 'rock'):
        return "computer"
    elif (user_choice == 'rock' and  computer_choice == 'scissors') or (user_choice == 'paper' and  computer_choice == 'rock') or (user_choice == 'scissors' and  computer_choice == 'paper'):
        return "user"


user_score = 0
computer_score = 0
for i in range(3):
    user = get_user_choice()
    computer = get_computer_choice()
    print("Computer choice :", computer)
    win = winner(user,computer)
    if win == "computer":
        user_score += 1
    elif win == "user":
        computer_score += 1
    
if user_score > computer_score :
    print("User score is ", user_score)
    print("\033[91m {}\033[00m" .format("user wins"))
elif computer_score > user_score :
    print("Computer score is ", computer_score)
    print("\033[91m {}\033[00m" .format("computer wins"))
else:
    print("\033[91m {}\033[00m" .format(" Game die"))