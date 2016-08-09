#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(count=0):
    print(username, "walk through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print(username, 'take the stairs')
        if (count > 0):
            print("but you're not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if next == "back door":
        back_room()


def gold_room():
    print("This room is full of gold.  How much does", username, "take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, {} wins!".format(username))
        exit(0)
    else:
        dead(username, "greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is {} going to move the bear?".format(username))
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or  next == "honey":
            dead("The bear looks at {} then slaps your face off.".format(username))
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. {} can go through it now.".format(username))
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open" or  next == "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
            print("{} finds a mysterious door and goes for it".format(username))
            infinite_stairway_room(5)


def cthulhu_room():
    print("Here {} sees the great evil Cthulhu.".format(username))
    print("He, it, whatever stares at {} and {} goes insane.".format(username))
    print("{}! Do you flee for your life or eat your head?".format(username))

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def back_room():
    print("This room is filled with awesome programmers".format(username))
    print("Welcome {} to the amazing world of Python!!".format(username))

    next = input("> ")

    if "code" in next:
        print("{} starts coding in python and loves it!!".format(username))
    elif next == "never leave":
        print("{} never wants to leave the room!".format(username))
    else:
        exit(0)


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
username = input("Hey there! Please enter your name\n")
def main():
    # START the TextAdventure game
    print("{}, you are in a dark room.".format(username))
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("{} stumbles around the room until they starve.".format(username))

if __name__ == '__main__':
    main()
