################################################
## Author: Michael Nickins                    ##
## Last Edited: 09NOV2024                     ##
## This file contains all data for Chapter 2. ##
################################################



from global_database import player, get_random_npc_name, select_murder_weapon, hotel_names, bar_names, city_names, gun_store_names, display_chapter_visits
import random, time, loading, chapter1, chapter3, chapter4

random_gun_store = random.choice(gun_store_names)

global npc_name
npc_name = get_random_npc_name()

def start_chapter():
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

        choice = input("Enter your choice: ").strip()

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


def talk_to_bartender(npc_name):
    print(f"""You talk to {npc_name}. They confirm that the victim was in {chapter1.random_bar} at that time.
They mention that the person they were with were talking about just coming from {random_gun_store}.""")
    player.add_evidence(1)
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