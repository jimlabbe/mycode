#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    swapper = Cheat_Swapper()
    # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()
    sevener = Cheat_Sevens()
    # track scores for both players
    swapper_score = 0
    loaded_dice_score = 0
    sevener_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        sevener.roll()

        swapper.cheat()
        loaded_dice.cheat()
        sevener.cheat()
    # sort the scores 
        sorted_scores = []
        sorted_scores.append(sum(swapper.get_dice()))
        sorted_scores.append(sum(loaded_dice.get_dice()))
        sorted_scores.append(sum(sevener.get_dice()))
        result = sorted_scores.index(max(sorted_scores))
    """Remove # before print statements to see simulation running
    Simulation takes approximately one hour to run with print
    statements or ten seconds with print statements
    ommented out"""
    
        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if result == 0:
            swapper_score+=1
        elif result == 1:
            loaded_dice+=1
        else:
            #print("Loaded dice wins!")
            sevener+= 1
        print(result)
        print
        game_number += 1



    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")
    print(f"Sevener won: {sevener_score}")

    # determine the winner
    if sevener_score > loaded_dice_score or swapper_score:
        print("Sevener won most games")
    elif swapper_score > loaded_dice_score or sevener_score:
        print("Swapper won most games")
    else:
        print("Loaded dice won most games")

if __name__ == "__main__":
    main()

