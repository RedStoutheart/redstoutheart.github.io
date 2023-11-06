import random
import time
def roll():
    min_val = 1
    max_lav = 6
    roll = random.randint(min_val, max_lav)

    return roll

try:
    informantion = int(input("Do you need info (1): "))

    if informantion != 1:
        pass
    else:
        print('''
How to Play
***********
-In this game you constatly roll a dice unless you don't want to!
-A dice has values of 1 to 6!
-If you reach or exeed 50 you win!
-First player who reaches wins!
-If you roll 1 then your total score will set to 0!
-This game can be played with at least 2 players and up to 4!
-Have Fun!\n''')
        time.sleep(10)
        
except ValueError:
    pass



while True:
    players = input("Enter the number of players(1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players!")

max_score = 5 
player_scores = [0 for _ in range(players)]

while max(player_scores) <= max_score:

    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has just started!")
        print(f'Your totat score is: {player_scores[player_idx]}\n')
        current_score = 0

        while True:
            should_roll = input("\nWould you like to roll (y)? ")
            
            if should_roll.lower() != 'y' or 'yy':
                break
            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break

            else:
                current_score += value
                print(f"You rolled '{value}' :)")

            print('Your score is', current_score)
        player_scores[player_idx] += current_score

    print('Your total score is: ', current_score)


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player{winning_idx + 1} is the winner with a score of:{max_score}")
