################################################
## Author: Michael Nickins                    ##
## Last Edited: 09NOV2024                     ##
## This file contains all data for Chapter 5. ##
################################################



from global_database import player, get_random_npc_name, select_murder_weapon, hotel_names, bar_names, city_names, gun_store_names, display_chapter_visits
import random, time, loading, chapter1, chapter2, chapter3, chapter4

global npc_name
npc_name = get_random_npc_name()

def start_chapter():
    player.mark_chapter_visited("chapter5")
    print("Chapter 5: Grabbing a Viper by it's Tail")
    print(f"""After visiting {chapter4.npc_name}, your contact at the {chapter1.random_city} police precinct, you successfully brought enough evidence to bear
to convince them to go with you to bring the killer in.""")

    ## DEBUG ## display_chapter_visits() ## DEBUG ##

    while True:
        ## Display menu options with numbers, specifying already selected choices.
        print("\nChoose an action:")

        print("1. Knock on the front door." + (" (already selected)" if player.is_choice_selected("chapter5", "is_anyone_home") else ""))

        if player.is_choice_selected("chapter5", "is_anyone_home"):
            print("2. Talk to the suspect." + (" (already selected)" if player.is_choice_selected("chapter5", "talk_to_suspect") else ""))

        if player.is_choice_selected("chapter5", "talk_to_suspect"):
            print("3. Look around the residence." + (" (already selected)" if player.is_choice_selected("chapter5", "look_around_residence") else ""))

        if player.is_choice_selected("chapter5", "is_anyone_home"):
            print("4. Arrest the suspect. (Finish Game)")

        print("Q. Quit game")

        choice = input("Enter your choice: ").strip()

        if choice == "1" and not player.is_choice_selected("chapter5", "is_anyone_home"):
            knock_on_door()
            player.mark_choice_selected("chapter5", "is_anyone_home")
        elif choice == "2" and not player.is_choice_selected("chapter5", "talk_to_suspect"):
            talk_to_suspect(npc_name)
            player.mark_choice_selected("chapter5", "talk_to_suspect")
        elif choice == "3" and not player.is_choice_selected("chapter5", "look_around_residence"):
            look_around_residence()
            player.mark_choice_selected("chapter5", "look_around_residence")
        elif choice == "4" and not player.is_choice_selected("chapter5", "arrest_suspect"):
            confirm_choice = input("Are you sure you want to arrest them? (Y/N): ").strip().upper()

            if confirm_choice == "Y":
                print("Placing them under arrest...")
                arrest_suspect()
                break
            else:
                print("Not yet...")

        elif choice.upper() == "Q":
            print("Thank you for playing! Exiting game...")
            break
        else:
            print("Invalid choice or action already completed. Please select another option.")

def knock_on_door():
    print("""You slam your fist against the front door. It takes a few minutes but someone eventually cracks open the door.""")
    time.sleep(1)
    print()

def talk_to_suspect(npc_name):
    print(f"""You confirm if they're {npc_name}, which they rudely do.""")
    time.sleep(2)
    print("You ask where they were at the time of the murder.")
    time.sleep(2)
    print(f"They offer a crude alibi of being at {chapter1.random_bar} all night.")
    time.sleep(2)
    print("You ask if they left with anyone, to which they reply with a negative.")
    time.sleep(2)
    print(f"With a raised eyebrow, you give out that the bartender, {chapter2.npc_name}, plainly saw you leave with someone.")
    time.sleep(2)
    print(f"They try to slam the door in your face, but you barge your way in, {chapter4.npc_name} groaning in annoyance.")
    player.add_evidence(1)
    print()

def look_around_residence():
    location = chapter1.weapon.get("location", "tucked in a corner of the house.")
    print(f"""As {chapter4.npc_name} distracts {npc_name}, you quickly scour the house, finding the weapon
{location}""")
    player.add_evidence(1)
    print()

def arrest_suspect():
    if player.evidence_value >= 9:
        print(f"""You and {chapter4.npc_name} placed {npc_name} under arrest. After a thorough interrogation and upon being
presented a mountain of evidence, they confessed to the murder.""")
        time.sleep(2)
        print("Congratulations! You solved the case!")
    else:
        print(f"""You and {chapter4.npc_name} placed {npc_name} under arrest. Despite a thorough interrogation, there wasn't
enough evidence of a conviction.""")
        time.sleep(2)
        print("Not quite! Try again!")