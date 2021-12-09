# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

def intro():
    print("\n\tWelcome to Tine's Guessing Number")
    name = input("\n\tHello! What is your name? \n\t>> ")
    print(f"Well {name.title()} before we begin, let's learn how to play the game.")
    print("The computer will ask you for a number, and you will have to guess what it will give you.")

def main():
    intro()

main()