################################################
## Author: Michael Nickins                    ##
## Last Edited: 09NOV2024                     ##
## This file contains all data for Chapter 2. ##
################################################



## Imports Python's 'random' and 'time' libraries and directly imports the 'loading', 'chapter1', 'chapter3', and 'chapter4' .py files.
## Imports a number of lists and functions from 'global_database.py'.
from global_database import player, get_random_npc_name, select_murder_weapon, hotel_names, bar_names, city_names, gun_store_names, display_chapter_visits
import random, time, loading, chapter1, chapter3, chapter4

## Defines variable calling a gun store list entry at random.
random_gun_store = random.choice(gun_store_names)

## Globally defines the 'get_random_npc_name' function to a variable.
global npc_name
npc_name = get_random_npc_name()

## Defines a function to start the chapter.
def start_chapter():
    ## Calls the 'mark_chapter_visited' function from the Player class with the specified 'chapter2' entry.
    player.mark_chapter_visited("chapter2")
    print("Chapter 2: A Den of Sin")
    print(f"""After investigating the murder of a patron at {chapter1.random_hotel},
you move on to {chapter1.random_bar}, a nearby bar, for any possible leads.""")
    
    ## DEBUG ## display_chapter_visits() ## DEBUG ##

    while True:
        ## Display menu options with numbers, specifying already selected choices.
        print("\nChoose an action:")
        
        if npc_name and not player.is_choice_selected("chapter2", "talk_to_bartender"):
            print("1. Talk to the bartender.")
        else:
            print("1. Talk to the bartender. (already selected)")
        
        print("2. Go to the bathroom" + (" (already selected)" if player.is_choice_selected("chapter2", "go_to_the_bathroom") else ""))
        print("3. Talk to the other patrons" + (" (already selected)" if player.is_choice_selected("chapter2", "talk_to_patrons") else ""))
        print(f"4. Go back to {chapter1.random_hotel} (Return to Chapter 1)")

        ## Option only appears if the players selects the "talk to bartender" option.
        if player.is_choice_selected("chapter2", "talk_to_bartender"):
            print(f"5. Give {random_gun_store} a visit (Move on to Chapter 3)")
        
        ## Return to a future chapter if it has been visited.
        if player.chapter_visits["chapter3"] > 0:
            print(f"6. Go back to {random_gun_store} (Return to Chapter 3)")
        if player.chapter_visits["chapter4"] > 0:
            print(f"7. Go back to the {chapter1.random_city} police precinct (Return to Chapter 4)")
        
        print("Q. Quit game")

        ## Hooks the user input to a variable.
        choice = input("Enter your choice: ").strip()

        ## Specifies which inputs are allowed and their effects.
        if choice == "1" and npc_name and not player.is_choice_selected("chapter2", "talk_to_bartender"):
            talk_to_bartender(npc_name)
            player.mark_choice_selected("chapter2", "talk_to_bartender")
        elif choice == "2" and not player.is_choice_selected("chapter2", "go_to_the_bathroom"):
            go_to_the_bathroom()
            player.mark_choice_selected("chapter2", "go_to_the_bathroom")
        elif choice == "3" and not player.is_choice_selected("chapter2", "talk_to_patrons"):
            talk_to_patrons()
            player.mark_choice_selected("chapter2", "talk_to_patrons")
        elif choice == "4" and player.chapter_visits["chapter1"] > 0:
            print(f"Returning to {chapter1.random_hotel}...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter1.start_chapter()
            break
        elif choice == "5" and player.is_choice_selected("chapter2", "talk_to_bartender"):
            print("Advancing to Chapter 3...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter3.start_chapter()
            break
        elif choice == "6" and player.chapter_visits["chapter3"] > 0:
            print(f"Returning to {random_gun_store}...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter3.start_chapter()
            break
        elif choice == "7" and player.chapter_visits["chapter4"] > 0:
            print(f"Returning to the {chapter1.random_city} police precinct...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter4.start_chapter()
            break
        elif choice.upper() == "Q":
            print("Thank you for playing! Exiting game...")
            break
        else:
            print("Invalid choice or action already completed. Please select another option.")

## Defines a function for user interaction.
def talk_to_bartender(npc_name):
    print(f"""You talk to {npc_name}. They confirm that the victim was in {chapter1.random_bar} at that time.
They mention that the person they were with were talking about just coming from {random_gun_store}.""")
    player.add_evidence(1) ## Adds a positive value to the evidence counter.
    time.sleep(1)
    print()

def go_to_the_bathroom():
    print("You go to the bathroom.")
    time.sleep(2)
    print("Nothing of importance happens.")
    time.sleep(1)
    print()

def talk_to_patrons():
    print("You talk to some nearby patrons. They each give a physical description of the individual in question with varying reliability.")
    player.add_evidence(1)
    time.sleep(1)
    print()