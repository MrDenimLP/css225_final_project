################################################
## Author: Michael Nickins                    ##
## Last Edited: 09NOV2024                     ##
## This file contains all data for Chapter 1. ##
################################################



## Imports Python's 'random' and 'time' libraries and directly imports the 'loading', 'chapter2', 'chapter3', and 'chapter4' .py files.
## Imports a number of lists and functions from 'global_database.py'.
from global_database import player, get_random_npc_name, select_murder_weapon, hotel_names, bar_names, city_names, gun_store_names, display_chapter_visits
import random, time, loading, chapter2, chapter3, chapter4

## Defines variables calling certain list entries at random.
random_hotel = random.choice(hotel_names)
random_bar = random.choice(bar_names)
random_city = random.choice(city_names)

## Globally defines the 'select_murder_weapon' function to a variable.
global weapon
weapon = select_murder_weapon()

## Defines a function to start the chapter.
def start_chapter():
    ## Calls the 'mark_chapter_visited' function from the Player class with the specified 'chapter1' entry.
    player.mark_chapter_visited("chapter1")
    print("Chapter 1: Welcome to the investigation")
    print(f"You are in the city of {random_city}, at {random_hotel} where an individual was found murdered in their hotel room. A guest in an adjoining room found the victim.")
    
    ## DEBUG ## display_chapter_visits() ## DEBUG ##

    while True:
        ## Displays menu options with numbers, specifying already selected choices.
        print("\nChoose an action:")
        npc_name = get_random_npc_name()
        if npc_name and not player.is_choice_selected("chapter1", "talk_to_guests"):
            print("1. Talk to guest")
        else:
            print("1. Talk to guest (already selected)")

        print("2. Examine the room" + (" (already selected)" if player.is_choice_selected("chapter1", "examine_room") else ""))
        print("3. Investigate the body" + (" (already selected)" if player.is_choice_selected("chapter1", "investigate_body") else ""))
        
        ## Option appears only if the player selects the "investigate the body" option.
        if player.is_choice_selected("chapter1", "investigate_body"):
            print("4. Pay the bar a visit (Move on the Chapter 2)")

        ## Return to a future chapter if it has been visited.
        if player.chapter_visits["chapter2"] > 0:
            print(f"5. Go back to {random_bar} (Return to Chapter 2)")
        if player.chapter_visits["chapter3"] > 0:
            print(f"6. Go back to {chapter2.random_gun_store} (Return to Chaper 3)")
        if player.chapter_visits["chapter4"] > 0:
            print(f"7. Go back to the {random_city} police precinct (Return to Chapter 4)")

        print("Q. Quit game")

        ## Hooks the user input to a variable.
        choice = input("Enter your choice: ").strip()

        ## Specifies which inputs are allowed and their effects.
        if choice == "1" and npc_name and not player.is_choice_selected("chapter1", "talk_to_guests"):
            talk_to_guests(npc_name)
            player.mark_choice_selected("chapter1", "talk_to_guests")
        elif choice == "2" and not player.is_choice_selected("chapter1", "examine_room"):
            examine_room()
            player.mark_choice_selected("chapter1", "examine_room")
        elif choice == "3" and not player.is_choice_selected("chapter1", "investigate_body"):
            investigate_body()
            player.mark_choice_selected("chapter1", "investigate_body")
        elif choice == "4" and player.is_choice_selected("chapter1", "investigate_body"):
            print("Advancing to Chapter 2...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter2.start_chapter()
            break
        elif choice == "5" and player.chapter_visits["chapter2"] > 0:
            print(f"Returning to {random_bar}...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter2.start_chapter()
            break
        elif choice == "6" and player.chapter_visits["chapter3"] > 0:
            print(f"Returning to {chapter2.random_gun_store}")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter3.start_chapter()
            break
        elif choice == "7" and player.chapter_visits["chapter4"] > 0:
            print(f"Returning to the {random_city} police precinct...")
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
def talk_to_guests(npc_name):
    sound = weapon.get("sound", "a mysterious sound was heard.") ## Uses the previously defines global variable to retrieve the 'sound' entry.
    print(f"You talk to {npc_name} and gather information about the noise complaint. They state that they heard {sound}")
    player.add_evidence(1) ## Adds a positive value to the evidence counter.
    time.sleep(1)
    print()

def examine_room():
    print("""You examine the room and gather photographic evidence.
A coffee table is turned over. The tv is still playing a noir film at max volume.
Their belongings are undisturbed. A painting on the wall is tilted with cracked glass.""")
    player.add_evidence(1)
    time.sleep(1)
    print()

def investigate_body():
    print(f"""You investigate the body and find clues about the weapon used.
Going through their pockets, you find a receipt for a bar called {random_bar}, located nearby.""")
    player.add_evidence(1)
    time.sleep(1)
    print()