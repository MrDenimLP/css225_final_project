################################################
## Author: Michael Nickins                    ##
## Last Edited: 09NOV2024                     ##
## This file contains all data for Chapter 4. ##
################################################



## Imports Python's 'random' and 'time' libraries and directly imports the 'loading', 'chapter1', 'chapter2', 'chapter3', and 'chapter5' .py files.
## Imports a number of lists and functions from 'global_database.py'.
from global_database import player, get_random_npc_name, select_murder_weapon, hotel_names, bar_names, city_names, gun_store_names, display_chapter_visits
import random, time, loading, chapter1, chapter2, chapter3, chapter5

## Globally defines the 'get_random_npc_name' function to a variable.
global npc_name
npc_name = get_random_npc_name()

## Defines a function to start the chapter.
def start_chapter():
    ## Calls the 'mark_chapter_visited' function from the Player class with the specified 'chapter34' entry.
    player.mark_chapter_visited("chapter4")
    print("Chapter 4: Into the Pig Pen")
    print(f"""After visiting {chapter2.random_gun_store}, you called your police contact and scheduled a visit
at the {chapter1.random_city} police precinct.""")

    ## DEBUG ## display_chapter_visits() ## DEBUG ##

    while True:
        ## Display menu options with numbers, specifying already selected choices.
        print("\nChoose an action:")

        if npc_name and not player.is_choice_selected("chapter4", "talk_to_contact"):
            print("1. Talk to your contact")
        else:
            print("1. Talk to your contact (already selected)")
        
        print("2. Present evidence" + (" (already selected)" if player.presented_sufficient_evidence else ""))
        
        if player.presented_sufficient_evidence:
            print("3. Depart to suspect's location (Move on to the final chapter)")

        print(f"4. Go back to {chapter1.random_hotel} (Return to Chapter 1)")
        print(f"5. Go back to {chapter1.random_bar} (Return to Chapter 2)")
        print(f"6. Go back to {chapter2.random_gun_store} (Return to Chapter 3)")

        print("Q. Quit game")

        ## Hooks the user input to a variable.
        choice = input("Enter your choice: ").strip()

        ## Specifies which inputs are allowed and their effects.
        if choice == "1" and npc_name and not player.is_choice_selected("chapter4", "talk_to_contact"):
            talk_to_contact(npc_name)
            player.mark_choice_selected("chapter4", "talk_to_contact")
        elif choice == "2" and not player.is_choice_selected("chapter4", "present_evidence"):
            present_evidence()
        elif choice == "3" and player.is_choice_selected("chapter4", "present_evidence"):
            confirm_choice = input("Are you sure you want to move on? (Y/N): ").strip().upper()

            if confirm_choice == "Y":
                print("Advancing to the final chapter...")
                for i in range(101):
                    loading.loading_bar(i, 100)
                    time.sleep(0.1)
                print(""" 

""")
                chapter5.start_chapter()
                break
            else:
                print("Not moving on yet...")
        elif choice == "4" and player.chapter_visits["chapter1"] > 0:
            print(f"Returning to {chapter1.random_hotel}...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter1.start_chapter()
            break
        elif choice == "5" and player.chapter_visits["chapter2"] > 0:
            print(f"Returning to {chapter1.random_bar}...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter2.start_chapter()
            break
        elif choice == "6" and player.chapter_visits["chapter3"] > 0:
            print(f"Returning to {chapter2.random_gun_store}...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter3.start_chapter()
            break
        elif choice.upper() == "Q":
            print("Thank you for playing! Exiting game...")
            break
        else:
            print("Invalid choice or action already completed. Please select another option.")

## Defines a function for user interaction.
def talk_to_contact(npc_name):
    print(f"""You talk to {npc_name}, your contact at the {chapter1.random_city} police precinct.
They hesitantly offer what the police already knows.""")
    player.add_evidence(1) ## Adds a positive value to the evidence counter.
    time.sleep(1)
    print()

def present_evidence():
    print("You present what evidence you've collected.")
    time.sleep(2)
    if player.evidence_value >= 5: ## Performs a check to see if the amount of evidence collected is higher than or equal to 5.
        print("They agree with your findings and offer their assistance in taking down the killer.")
        player.presented_sufficient_evidence = True ## Sets the boolean value of the 'presented_sufficient_evidence' parameter in the Player class to 'True'.
        player.mark_choice_selected("chapter4", "present_evidence")
    else:
        print("They don't quite believe you. (Do some more digging in the previous chapters)")
        player.presented_sufficient_evidence = False