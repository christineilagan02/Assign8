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
    separator()
    print(f"\n\t        Well \33[1m{name.title()}\33[0m before we begin, \n\t    let's learn how to play the game.\n")
    separator()
    instruction()
    print("\n\t         Are you ready to guess a number?")
    

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
    string = ("\n\t\33[3mThe computer will ask you for a number around 0 to 99,\n\t  and you will have to guess what it will give you.\33[0m\n")
    for letter in string:
        sleep(0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()

def ready():
    answer = input("\n\t       Kindly, type y for yes and n for no. \n\t         >> ")
    if answer.lower() == "y":
        return answer
    elif answer.lower() == "n":
        separator()
        print("\t\33[1m    Ok come back when you're ready! \33[0m")
        print("\t\33[1m\33[93m\33[3m           You can now exit.\33[0m")
        separator()
        sys.exit("\n")
    else: 
        print("\t\33[31m\33[1m         Sorry your input must be a y/n!\33[0m")
        return ready()

def separator():
    print("\t   \33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")

def _guess():
    guessesTaken = 0
    number = random.randrange(0, 99)


    while guessesTaken < 99:
        separator()
        guess = int(input("\t             Take a guess. \n\t           >> "))

        guessesTaken += 1

        if guess >= 0 and guess <=99:
            if guess < number:
                print("\t\33[1m\33[33m        Your guess is less than ")
                print("\t         the computer's number.\33[0m")
                continue
                
            if guess > number:
                print("\t\33[1m\33[34m      Your guess is greater than ")
                print("\t        the computer's number.\33[0m")
                continue
                
            if guess == number:
                break

        else:
            print("\t\33[1m\33[31mThe number you entered is not included ")
            print("\t        in the predicted number.")
            print("\t       Just select from 0 to 99.\33[0m")
            continue

    if guess == number:
        guessesTaken = str(guessesTaken)
        print("\t\33[1m\33[32m               Good Job!")
        print(f"\t   You guess the number in {guessesTaken} guesses!\33[0m")
        separator()
        print("\n")


def main():
    intro()
    ready()
    _guess()

main()