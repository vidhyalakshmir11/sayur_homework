# Problem #2
# Two player dice game.
# Each player will roll the die (numbers from 1 to 6)
# Points are added to each roll.
# 1 - 1 pt
# 2 - 5 pts
# 3 - 15 pts
# 4 - (-15) pts
# 5 - (-5) pts
# 6 - (-1) pts

# Find which player scores 100 first and how many time they had to roll the die.
# Hint - use random numbers to generate the die (no need to get user input)
# Use Arrays and while loop.

import random

def dice_roll():
    score1 = 0
    score2 = 0
    round = 0
    
    while score1 < 100 and score2 < 100:
        round=round+1
        player1 = random.randint(1, 6)
        player2 = random.randint(1, 6)
        
        #print("Player 1 choice:", player1)
        #print("Player 2 choice:", player2)
        if player1 == 1 or player2 == 1 :
            if player2 == 1:
                score2 += 1
            else :
                score1 += 1
        elif player1 ==2 or player2 == 2: 
            if player1 == 2:
                score1 += 5
            else :
                score2 +=5
        elif player1 ==3 or player2 == 3: 
            if player1 == 3:
                score1 += 15
            else :
                score2 += 15
        elif player1 ==4 or player2 == 4: 
            if player1 == 4:
                score1 -= 15
            else :
                score2 -= 15
        elif player1 ==5 or player2 == 5: 
            if player1 == 5:
                score1 -= 5
            else :
                score2 -= 5
        elif player1 ==6 or player2 == 6: 
            if player1 == 6:
                score1 -= 1
            else :
                score2 -= 1
        
        
    print("Player 1 total score:", score1)
    print("Player 2 total score:", score2)
    print()

    if score1 >= 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    print("Number of rounds:", round)

dice_roll()
  