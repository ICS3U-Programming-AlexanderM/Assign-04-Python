#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Jan 11, 2022
# This program gets the user to enter a number of sides.
# It then simulates two die with that number of sides
# and rolls then until it gets doubles.
import random

# declare global variables
loop_counter = 0
sides_string = 0
sides = 0


# function to get and check user input
def user_input():
    # declare global variables
    global sides_string
    global sides

    sides_string = input("Enter the number of sides on each die: ")

    # error checking
    try:
        sides = int(sides_string)
    except Exception:
        print("Invalid input")
        return user_input()
    else:
        if sides <= 0:
            print("Number must be positive.")
            return user_input()


# The Die Is Cast
# function to roll the dice
def alea_iacta_est():
    # declare global variables
    global loop_counter

    # loop
    while True:
        # increase loop_counter
        loop_counter = loop_counter + 1

        # roll the dice
        roll_a = random.randint(1, sides)
        roll_b = random.randint(1, sides)
        print("{} and {}". format(roll_a, roll_b))
        if roll_a == roll_b:
            print("It took {} tries to get doubles.". format(loop_counter))
            break


def main():
    # call functions
    user_input()
    alea_iacta_est()


if __name__ == "__main__":
    main()
