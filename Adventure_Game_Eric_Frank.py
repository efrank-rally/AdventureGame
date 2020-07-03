import random
import sys
import time

monsters = ["orcs", "knolls", "goblins", "hobgoblins"]
weapons = ["spear", "mace", "battle axe", "thowing axe"]
monster = random.choice(monsters)
weapon = random.choice(weapons)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print("You have discovered a large cavern near town, so you enter it")
    time.sleep(2)
    print("You see a large wooden door and a small wooden door")
    time.sleep(2)
    print(
        "You are looking to destroy the dangerous "
        f"leader of the {monster}, "
        "so you can protect the town"
    )
    time.sleep(2)
    print("Of course you have to find a weapon first")
    time.sleep(2)


def choice_fight_run(items):
    print("What would you like to do?")
    fight_run = input("Enter 1 to attack him\n"
                      "Enter 2 to run for your life?\n")
    if fight_run == '1':
        if "weapon" in items:
            print_pause(
                f"You pull out your {weapon} "
                f"and throw it at the leader of the {monster}"
            )
            print_pause(
                f"The {weapon} hits him in the head "
                "and he falls down dead"
            )
            print_pause("Congrats! You've won the game and saved the town")
            play_again()
        else:
            print_pause(
                f"The leader of the {monster} "
                f"swings his {weapon} at you"
            )
            print_pause(
                "He hits you with amazing force "
                "and your life leaves you instantly"
            )
            print_pause("Sorry, you died and lost the game")
            print_pause("You must find a weapon in order to defeat him")
            play_again()
    elif fight_run == '2':
        print_pause(
            "You run back to the cavern, "
            "but luckily your attacker decides not to follow"
        )
        choice(items)
    else:
        print_pause("Sorry, that is an invalid response")
        choice_fight_run(items)


def large_door(items):
    print_pause("You enter a very large room with "
                "many lit torches lining the walls")
    print_pause("You hear some grumbling noises ahead of you")
    print_pause(f"Suddenly the leader of the {monster} pops out of nowhere")
    print_pause(f"He starts running to attack you with his battle axe")
    choice_fight_run(items)


def small_door(items):
    if "weapon" in items:
        print_pause("You've been here before. Nothing new to see here")
        print_pause("You proceed back to the large cavern")
        choice(items)
    else:
        print_pause("You enter a fairly small room "
                    "with many bookshelves full of old books")
        print_pause(f"You notice there is a small table with a {weapon} on it")
        print_pause(
            f"You decide to grab the {weapon} off the table "
            "and walk back out to the large cavern"
        )
        items.append("weapon")
        choice(items)


def choice(items):
    print("What would you like to do?")
    player_choice = input("Enter 1 to open and proceed through "
                          "the large wooden door\n"
                          "Enter 2 to open and proceed through "
                          "the small wooden door\n")
    if player_choice == '1':
        large_door(items)
    elif player_choice == '2':
        small_door(items)
    else:
        print_pause("Sorry, that is an invalid response")
        choice(items)


def play_again():
    player_input = input("Would you like to play this game again? "
                         "Please enter y or n.\n").lower()
    if player_input == 'y':
        print_pause("Great! Here we go again!")
        play_game()
    elif player_input == 'n':
        print_pause("Sorry to see you go. Catch you next time")
        sys.exit()
    else:
        print_pause("Sorry, that is an invalid response")
        play_again()


def play_game():
    items = []
    intro()
    choice(items)


play_game()
