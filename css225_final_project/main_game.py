#####################################
## Author: Michael Nickins         ##
## Last Edited: 09NOV2024          ##
## This file initializes the game. ##
#####################################



from global_database import player, set_player_name
import chapter1, chapter2, chapter3, chapter4, chapter5

def start_game():
    player_name = input("Enter your name: ")
    set_player_name(player_name)
    print(f"Welcome, {player_name}. Let’s start the game!")
    chapter1.start_chapter()

if __name__ == "__main__":
    start_game()
