import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    print_pause("You find yourself in middle of huge forest.")
    print_pause("It was very dark, cold & scary with animal sounds coming.")
    print_pause("You found dagger on path & you took it for safety.")
    print_pause("Paths divides two way in front of you. Left & Right.")
    print_pause("In left path there is hunter cave.")
    print_pause("In right path there is a wooden house.")


def path(item, option):
    print_pause("\nWhich path you want to take? Left or Right.")
    print_pause("\nEnter 1 to take left path ahead of you.")
    print_pause("Enter 2 to take right path ahead of you.")
    while True:
        path = input("(Please Enter '1' Or '2'.)\n")
        if path == "1":
            cave(item, option)
            break
        elif path == "2":
            house(item, option)
            break


def house(item, option):
    print_pause("\nYou knocked the house door!")
    print_pause("Out of the door steps a giant " + option + ".")
    print_pause("The " + option + " attacks you!\n")
    print_pause("Do you want to (1) fight or (2) run away?\n")
    while True:
        task = input("(Please enter '1' or '2'.)\n")
        if task == "1":
            fight(item, option)
            break
        elif task == "2":
            run(item, option)
            break


def fight(item, option):
    if "weapon" in item:
        print_pause("\nThe " + option + " attacked you.")
        print_pause("You fought with great courage with magical sword.")
        print_pause("You claimed victory & you're free from danger.")
    else:
        print_pause("\nYou do your best...")
        print_pause("But your dagger is not enough!\n\n")
        print_pause("The End.\n\n")
    play_again()


def run(item, option):
    print_pause("\nYou're ran away in fear like a kid.'")
    path(item, option)


def cave(item, option):
    print_pause("\nYou went inside cave.\n")
    if "weapon" in item:
        print_pause(
            "You have been here before, and gotten all the"
            " good stuff. It's just an empty cave now.\n"
        )
    else:
        print_pause("You found a sharp magical sword in the cave.")
        print_pause("You take the sword with you & discarded your old dagger!")
        item.append("weapon")
    print_pause("You left the cave and go back to the path!")
    path(item, option)


def play_again():
    play = input("Would you like to play again? (y/n)\n").lower()
    if play == "y":
        print_pause("\nGood luck for another game!\n")
        play_game()
    elif play == "n":
        print_pause("\nThank you for playing! See you next time.\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["troll", "wicked fairie", "pirate", "dragon"])
    intro()
    path(item, option)


play_game()
