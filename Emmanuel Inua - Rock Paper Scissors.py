
# We need to create a set of random choices for the computer. We'll import a module

import random

# so the game can be replayed multiple times, we create a loop and possible responses to break the loop.

while True:
    print ("Are you ready to play a game of Rock, Paper Scissors with me")
    play = input("yes or no:  ")

    if play == "No" or play == "no" or play == "NO":
        break


    # Now for the user's input

    your_choice = input("Enter a choice (rock, paper, scissors):")

    # Now for the computer's input

    pos_choices = ["rock", "paper", "scissors"]
    comp_choice = random.choice(pos_choices)

    # we print the choices of both players, helps to see if we have errors.

    print (f"\nYou chose {your_choice}, computer chose {comp_choice}.\n")

    if your_choice == comp_choice:
        print (f"Both players selected {your_choice}. It's a tie!! for now.")
    elif your_choice == "rock":
        if comp_choice == "scissors":
            print ("rock smashes scissors, you win kiddo!")
        else:
            print ("paper covers rock!! You lose this round.")
    elif your_choice == "paper":
        if comp_choice == "rock":
            print ("paper covers rock, you win kiddo!")
        else:
            print ("scissors cuts paper!! You lose this round.")
    elif your_choice == "scissors":
        if comp_choice == "paper":
            print ("scissors cuts paper, you win kiddo!")
        else:
            print ("rock crushes scissors!! you lose this round.")

