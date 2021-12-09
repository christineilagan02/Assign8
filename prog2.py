# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import sys

def intro():
    print("\n\tWelcome to Tine's Guessing Number")
    name = input("\n\tHello! What is your name? \n\t>> ")
    print(f"Well {name.title()} before we begin, let's learn how to play the game.")
    instruction()
    print("Are you ready to guess a number?")

def instruction():
    from time import sleep
    string = ("\n\t\33[3mThe computer will ask you for a number,\nand you will have to guess what it will give you.\33[0m\n")
    for letter in string:
        sleep(0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()

def ready():
    answer = input("\t\nKindly, type y for yes and n for no. \n\t    >> ")
    print("\n")
    if answer.lower() == "y":
        return answer
    elif answer.lower() == "n":
        print("\t Ok come back when you're ready! ")
        print("\t You can now exit.")
        sys.exit("\n")
    else: 
        print(" Sorry your input must be a y/n!")
        return ready()

def main():
    intro()
    ready()

main()