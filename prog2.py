# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import sys
import random

def intro():
    welcome()
    title()
    name = input("\n\t        Hello! What is your name? \n\t      >> ")
    print(f"\n\t        Well {name.title()} before we begin, \n\t    let's learn how to play the game.\n")
    instruction()
    print("Are you ready to guess a number?")

def welcome():
    from time import sleep
    string = ("\n\t\33[1m                Welcome to\33[0m")
    for letter in string:
        sleep(0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()

def title():
    title = "\t      \33[33moOo\33[0m \33[1mTine's Guessing Number\33[0m \33[33moOo\33[0m"
    print("\n\t\33[1m\33[33m oOo\33[0m---+---+---+---\33[1m\33[33moOo\33[0m---+---+---+---\33[1m\33[33moOo\33[0m")
    print(title)
    print("\t\33[1m\33[33m oOo\33[0m---+---+---+---\33[1m\33[33moOo\33[0m---+---+---+---\33[1m\33[33moOo\33[0m")

def instruction():
    from time import sleep
    string = ("\n\t\33[3mThe computer will ask you for a number around 0 to 99,\nand you will have to guess what it will give you.\33[0m\n")
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

def _guess():
    guessesTaken = 0
    number = random.randrange(0, 99)


    while guessesTaken < 99:
        guess = int(input("Take a guess."))

        guessesTaken += 1

        if guess >= 0 and guess <=99:
            if guess < number:
                print("greater than")
                continue
                
            if guess > number:
                print("less than")
                continue
                
            if guess == number:
                break

        else:
            print("The number you entered is not included in the predicted number. Just select from 0 to 99.")
            continue

    if guess == number:
        guessesTaken = str(guessesTaken)
        print(f"Good Job! You guess the number in {guessesTaken} guesses!")


def main():
    intro()
    ready()
    _guess()

main()