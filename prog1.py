# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random
import sys

NUMBER_OF_PICKS = 3
MIN_PICK = 0
MAX_PICK = 9

def intro():
    print("Welcome to Tine's Lottery")
    name = input("Kindly, enter your name: \n>> ")
    print(f"Hello {name.title()}! ") 
    print("Are you ready to play?")

def _try():
    answer = input("Kindly, type y for yes and n for no. \n>> ")
    if answer.lower() == "y":
        return answer
    elif answer.lower() == "n":
        print("You can now exit.")
        sys.exit()
    else: 
        print("Sorry your input must be a y/n!")
        return _try()

def title():
    title = "\t      \33[33m**\33[0m \33[1mTine's Lottery\33[0m \33[33m**\33[0m"
    print("\n\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
    print(title)
    print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")

def lottery_menu():
     menu_list = ["\t           \33[3m\33[1m1. Play\33[0m", "\t           \33[3m\33[1m2. Exit\33[0m"]
     print(menu_list[0])
     print(menu_list[1])

    



def main():
    intro()
    _try()
    title()
    lottery_menu()

main()