################################################
## Author: Michael Nickins                    ##
## Last Edited: 09NOV2024                     ##
## This file contains all data for Chapter 3. ##
################################################



## Imports Python's 'random' and 'time' libraries and directly imports the 'loading', 'chapter1', 'chapter2', and 'chapter4' .py files.
## Imports a number of lists and functions from 'global_database.py'.
from global_database import player, get_random_npc_name, select_murder_weapon, hotel_names, bar_names, city_names, gun_store_names, display_chapter_visits
import random, time, loading, chapter1, chapter2, chapter4

## Globally defines the 'get_random_npc_name' function to a variable.
global npc_name
npc_name = get_random_npc_name()

## Defines a function to start the chapter.
def start_chapter():
    ## Calls the 'mark_chapter_visited' function from the Player class with the specified 'chapter3' entry.
    player.mark_chapter_visited("chapter3")
    print("Chapter 3: It only takes One Bullet")
    print(f"""After getting a tip from {chapter2.npc_name}, the bartender of {chapter1.random_bar}, 
you head to the provided location, {chapter2.random_gun_store}.""")

    ## DEBUG ## display_chapter_visits() ## DEBUG ##

    while True:
        ## Display menu options with numbers, specifying already selected choices.
        print("\nChoose an action:")

        if npc_name and not player.is_choice_selected("chapter3", "talk_to_owner"):
            print("1. Talk to the owner")
        else:
            print("1. Talk to the owner (already selected)")
        
        print("2. Look at the logbook" + (" (already selected)" if player.is_choice_selected("chapter3", "look_at_logbook") else ""))
        print("3. Call your police contact" + (" (already selected)" if player.is_choice_selected("chapter3", "call_police_contact") else ""))
        
        if player.is_choice_selected("chapter3", "call_police_contact"):
            print(f"4. Go to the {chapter1.random_city} police precinct (Move on to Chapter 4)")
        
        print(f"5. Go back to {chapter1.random_hotel} (Return to Chapter 1)")
        print(f"6. Go back to {chapter1.random_bar} (Return to Chapter 2)")

        ## Return to a future chapter if it has been visited.
        if player.chapter_visits["chapter4"] > 0:
            print(f"7. Go back to the {chapter1.random_city} police precinct")

        print("Q. Quit game")

        ## Hooks the user input to a variable.
        choice = input("Enter your choice: ").strip()

        ## Specifies which inputs are allowed and their effects.
        if choice == "1" and npc_name and not player.is_choice_selected("chapter3", "talk_to_owner"):
            talk_to_owner(npc_name)
            player.mark_choice_selected("chapter3", "talk_to_owner")
        elif choice == "2" and not player.is_choice_selected("chapter3", "look_at_logbook"):
            look_at_logbook()
            player.mark_choice_selected("chapter3", "look_at_logbook")
        elif choice == "3" and not player.is_choice_selected("chapter3", "call_police_contact"):
            call_police_contact()
            player.mark_choice_selected("chapter3", "call_police_contact")
        elif choice == "4" and player.is_choice_selected("chapter3", "call_police_contact"):
            print(f"Advancing to Chapter 4...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter4.start_chapter()
            break
        elif choice == "5" and player.chapter_visits["chapter1"]:
            print(f"Returning to {chapter1.random_hotel}...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter1.start_chapter()
            break
        elif choice == "6" and player.chapter_visits["chapter2"] > 0:
            print(f"Returning to {chapter1.random_bar}...")
            for i in range(101):
                loading.loading_bar(i, 100)
                time.sleep(0.1)
            print(""" 

""")
            chapter2.start_chapter()
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
def talk_to_owner(npc_name):
    print(f"""You talk to the owner, {npc_name}. They provide a description that roughly matches what you've received previously""")
    player.add_evidence(1) ## Adds a positive value to the evidence counter.
    time.sleep(1)
    print()

def look_at_logbook():
    print("""You take a look at the log book and find an entry the sole entry that matches the time.
You make a note of the person's name""")
    player.add_evidence(1)
    time.sleep(1)
    print()

def call_police_contact():
    print(f"You give your contact within the {chapter1.random_city} police a call. They offer to hear you out.")
    time.sleep(1)
    print()