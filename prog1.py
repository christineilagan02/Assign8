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
WINNINGS = 1,000,000

def intro():
    print("\n\t       Welcome to Tine's Lottery")
    separator()
    name = input("\n\t        Kindly, enter your name: \n\t    >> ")
    print(f"\n\t              Hello {name.title()}! ") 
    print("\t        Are you ready to play?")


def _try():
    answer = input("\t\n          Kindly, type y for yes and n for no. \n\t    >> ")
    print("\n")
    if answer.lower() == "y":
        quotes()
        return answer
    elif answer.lower() == "n":
        separator()
        print("\t    Ok come back when you're ready! ")
        print("\t           You can now exit.")
        separator()
        sys.exit("\n")
    else: 
        print("\t  Sorry your input must be a y/n!")
        return _try()


def quotes():
    from time import sleep
    string = ("\n\tCourage is the discovery that you may not win, \n\t    and trying when you know you can lose.\n\t                                   — Tom Krause\n")
    for letter in string:
        sleep(0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()


def title():
    title = "\t         \33[33moOo\33[0m \33[1mTine's Lottery\33[0m \33[33moOo\33[0m"
    print("\n\t\33[1m\33[33moOo\33[0m---+---+---+---\33[1m\33[33moOo\33[0m---+---+---+---\33[1m\33[33moOo\33[0m")
    print(title)
    print("\t\33[1m\33[33moOo\33[0m---+---+---+---\33[1m\33[33moOo\33[0m---+---+---+---\33[1m\33[33moOo\33[0m")


def lottery_menu():
     menu_list = ["\n\t               \33[3m\33[1m1. Play\33[0m", "\t               \33[3m\33[1m2. Exit\33[0m"]
     print(menu_list[0])
     print(menu_list[1])


def separator():
    print("\t   \33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
    

def play():
    while True:
        choice = input("\n\t        Enter your choice[1-2] \n\t    >> ")
        if choice == '1':
            string = "\n\t        [Play Pick {}]".format(NUMBER_OF_PICKS) + "selected!"
            dotted = "\n\t     ----------------------------"
            
            print(dotted,
                  string,
                  dotted)


            userNums = get_user_nums()
            winningNums = get_winning_nums() 
            checker(userNums, winningNums)
            
            try_again()
            

        elif choice == '2':
            print("\n")
            separator()
            print ("\t           You can now exit.")
            separator()
            sys.exit("\n")
                         
        print("       Error! Invalid input. Press any key to continue...\n")

def get_user_nums():
    userNums = []
    while len(userNums) < NUMBER_OF_PICKS:
        nums = input(f"\n\t       Pick a number {MIN_PICK} through {MAX_PICK} \n\t    >>  ")
        try:
            nums = int(nums)
        except:
            print("\t   Sorry your input must be an integer!")
            continue
        if MIN_PICK <= nums <= MAX_PICK:
            if nums not in userNums:
                userNums.append(nums)
            else:
                print("\tError! You have already picked this number")
        else:
            print("\t   Error! Your number was not in range")

    return sorted(userNums)


def get_winning_nums():
    return sorted(random.sample(range(MIN_PICK, MAX_PICK), NUMBER_OF_PICKS)) 


def checker(userNums, winningNums):
    if userNums == winningNums:
        print ("\n\t Congratulations! You Win ₱{}!".format(WINNINGS),
               "\n\t           Your numbers: ", userNums,
               "\n\tThe winning lottery numbers were: ", winningNums, "\n")
    else:
        print ("\n\t              Sorry, you lose...",
               "\n\t           Your numbers: ", userNums,
               "\n\tThe winning lottery numbers were: ", winningNums, "\n")


def try_again():
    answer = input("\n\t                Try again y/n. \n\t    >> ")
    if answer.lower() == "y":
        return play()
    elif answer.lower() == "n":
        separator()
        print("\t          Thanks for playing! ")
        separator()
        sys.exit("\n")
    else: 
        print("\t        Sorry your input must be a y/n!")
        return try_again()




def main():
    intro()
    _try()
    title()
    lottery_menu()
    separator()
    play()

main()