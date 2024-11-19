################################################################
## Author: Michael Nickins                                    ##
## Last Edited: 10NOV2024                                     ##
## This file contains information that will be used globally. ##
################################################################



## Imports Python's 'random' library.
## Imports the Player class from 'player.py'.
import random
from player import Player

## Defines the imported 'Player' class into 'player' for easier coding.
player = Player()

## NPC names list for random selection.
npc_names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Drew",
    "Dwayne", "Amanda", "Gloria", "Anthony", "Mitch", "Cole"]
used_npc_names = []


## Nested Array for murder weapon selection.
murder_weapon = {
    "knife" : {
        "name" : "chef's knife",
        "sound" : "the sound of a muffled thud and then some screams and cries.",
        "location" : "soaking in the kitchen sink which was filled with soapy water and bleach."
    },
    "bat" : {
        "name" : "bat",
        "sound" : "a lot of dull thuds.",
        "location" : "leaning in the corner of the bathroom with a dirty rag underneath it."
    },
    "crowbar" : {
        "name" : "crowbar",
        "sound" : "a bunch of thunks.",
        "location" : "sitting in the utility closet ontop of a tool box."
    },
    "firearm" : {
        "9mm" : {
            "type" : "pistol",
            "name" : "9mm pistol",
            "sound" : "a loud bang followed by silence.",
            "location" : "tossed under the sofa cushion in the living room."
        },
        "45_acp" : {
            "type" : "pistol",
            "name" : "Colt 1911",
            "sound" : "a sharp, echoing blast.",
            "location" : "tucked in the back of an upper shelf in the bedroom closet."
        },
        "38_special" : {
            "type" : "revolver",
            "name" : "Smith & Wesson Revoler",
            "sound" : "a loud crack and metallic click.",
            "location" : "left in the pocket of the coat hung by the front door."
        },
        "shotgun" : {
            "type" : "shotgun",
            "name" : "Sawed-off Shotgun",
            "sound" : "a chest-rattling boom.",
            "location" : "shoved under the bed wrapped up with dirty clothes."
        },
    }
}

## List of random city names.
city_names = [
    "Lakewood", "Pleasantville", "Oakwood", "Hillcrest", "Brooksville",
    "Ashland", "Brentwood", "Springfield", "Bridgeport", "Middletown",
    "Riverside", "Millville", "Greenville", "Foxborough", "Elkton",
    "Fairview", "Riverton", "Kingsville", "Centerville", "Clayton"
]

## List of random hotel names.
hotel_names = [
    "The Grand Plaza",
    "Sunset Inn",
    "Royal Palace Hotel",
    "Eagle's Nest Suites",
    "Palm Tree Resort",
    "Ocean Breeze Hotel",
    "The Gilded Tower",
    "Mountain View Lodge",
    "The Heritage House",
    "Silver Sands Hotel"
]

## List of random bar names.
bar_names = [
    "The Tipsy Pelican",
    "Rusty Anchor Tavern",
    "The Red Lantern",
    "Whiskey Row",
    "Night Owl Lounge",
    "The Driftwood Pub",
    "The Starlight Saloon",
    "The Last Stop",
    "Copper Coin Bar",
    "Bourbon & Branch"
]

## List of random gun store names.
gun_store_names = [
    "Ace's Armory",
    "Hunter's Haven",
    "The Bullet Barn",
    "Liberty Arms",
    "Precision Point Firearms",
    "Iron Sights Gun Shop",
    "The Ammo Depot",
    "True Shot Outfitters",
    "Defender's Choice",
    "Lock & Load Guns"
]

## Function to get a random NPC name.
def get_random_npc_name():
    remaining_names = list(set(npc_names) - set(used_npc_names))
    if remaining_names:
        selected_name = random.choice(remaining_names)
        used_npc_names.append(selected_name)
        return selected_name
    return None ## All names have been used.
    print("DEBUG: All NPC names used. You should not be seeing this.")

## Function to set player name.
def set_player_name(name):
    player.name = name

## Function to select the murder weapon.
def select_murder_weapon():
    weapon_type = random.choice(list(murder_weapon.keys()))  ## Randomly chooses a weapon type.

    ## Checks if the weapon type is "firearm", requiring selection of a specific caliber.
    if weapon_type == "firearm":
        caliber = random.choice(list(murder_weapon["firearm"].keys()))  ## Randomly chooses a caliber for firearms.
        selected_weapon = murder_weapon["firearm"][caliber]  ## Gets the firearm details.
    else:
        selected_weapon = murder_weapon[weapon_type]  ## For all other weapons, directly accesses the weapon details.
    
    ## Ensures the selected_weapon has the necessary keys with default values if any are missing.
    required_keys = {"name": "unknown weapon", "sound": "a mysterious sound", "location": "unknown location"}
    return {key: selected_weapon.get(key, default) for key, default in required_keys.items()}

## Displaying visit counts for each chapter.
def display_chapter_visits():
    print("Chapter Visit Counts:")
    for chapter, visits in player.chapter_visits.items():
        print(f"{chapter.capitalize()}: {visits} visits")
