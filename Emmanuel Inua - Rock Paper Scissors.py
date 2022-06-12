
# We need to create a set of random choices for the computer. We'll import a module
import random

choices = ["R", "P", "S"]
your_score = 0
comp_score = 0
tie = 0

# Let's define some functions
def game():
    global your_score
    global comp_score
    global tie

    # Now for the user's input

    your_choice = input("Enter a choice rock (R), paper (p), scissors (s) or end game (e): ")

    # Now for the computer's input

    comp_choice = random.choice(choices)

    # we print the choices of both players, helps to see if we have errors.

    print (f"\nYou chose {your_choice}, computer chose {comp_choice}.\n")

    if your_choice.upper() == comp_choice:
        tie += 1
        print (f"Both players selected {your_choice}. It's a tie!! for now.")
        game()
        
        
    else:
        if your_choice.upper() == "R":
            if comp_choice == "S":
                your_score += 1
                print ("rock smashes scissors, you win kiddo!")
                game()

            else:
                comp_score += 1
                print ("paper covers rock!! You lose this round.")
                game()

        elif your_choice.upper() == "P":
            if comp_choice == "R":
                your_score += 1
                print ("paper covers rock, you win kiddo!")
                game()

            else:
                comp_score += 1
                print ("scissors cuts paper!! You lose this round.")
                game()

        elif your_choice.upper() == "S":
            if comp_choice == "P":
                your_score += 1
                print ("scissors cuts paper, you win kiddo!")
                game()

            else:
                comp_score += 1
                print ("rock crushes scissors!! you lose this round.")
                game()

# now to break the loop and show scores.

        elif your_choice.upper() == "E":
            def endgame():
                print ("Game over.")
                print ("User scored: " + str(your_score))
                print ("AI scored: " + str(comp_score))
                print ("You Tied at: " + str(tie))
            endgame()

        else:
            print("invalid. try again!")
            game()
        
game()

