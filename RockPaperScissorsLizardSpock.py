from random import randint # import from random random integer module

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]  # creates a list of options for the game

game = True  # starts the game loop

while game == True:

    computer_decision = options[randint(0, 4)] # gets computers decision randomly using range 0 to 4 in the option list

    # gets user input
    player1_input = input("please enter an option from the following Rock,Paper,Scissors,Lizard,Spock: ")

    # if user enters the data in lower case form it will be accepted
    p1 = player1_input.lower()

    player = p1.capitalize()  # this will change the format to upper case  the data and stores it

    print("player 1 decision: ", player)  # prints the player 1 data in uppercase form
    print("computer's decision: ", computer_decision)  # does the same for the computers decision

# makes the round a tie
    if player == computer_decision:
        print("this round is a tie")

# determines winner / loser if rock is picked by user
    elif player == "Rock":

        if computer_decision == "Paper":
            print("You lose!", computer_decision, "covers", player)

        elif computer_decision == "Scissors":
            print("You win!", player, "smashes", computer_decision)

        elif computer_decision == "Lizard":
            print("You win!", player, "crushes", computer_decision)

        elif computer_decision == "Spock":
            print("You lose!", computer_decision, "vaporizes", player)

# gets winner/loser based on user picking paper
    elif player == "Paper":

        if computer_decision == "Scissors":
            print("You lose!", computer_decision, "cuts", player)

        elif computer_decision == "Rock":
            print("You win!", player, "covers", computer_decision)

        elif computer_decision == "Lizard":
            print("You lose!", computer_decision, "eats", player)

        elif computer_decision == "Spock":
            print("You win!", player, "disproves", computer_decision)


# gets winner/loser when user picks scissors
    elif player == "Scissors":

        if computer_decision == "Paper":
            print("You win!", player, "cuts", computer_decision)

        elif computer_decision == "Rock":
            print("You lose!", computer_decision, "crushes", player)

        elif computer_decision == "Lizard":
            print("You win!", player, "decapitates", computer_decision)

        elif computer_decision == "Spock":
            print("You lose!", computer_decision, "smashes", player)

    # gets winner/ loser based on user picking lizard

    elif player == "Lizard":

        if computer_decision == "Rock":
            print("You lose!", computer_decision, "crushes", player)

        elif computer_decision == "Paper":
            print("You win!", player, "eats", computer_decision)

        elif computer_decision == "Scissors":
            print("You lose!", computer_decision, "decapitates", player)

        elif computer_decision == "Spock":
            print("You win!", player, "poisons", computer_decision)


# gets winner/loser based of picking spock

        elif player == "Spock":

            if computer_decision == "Rock":
                print("You win!", player, "vaporizes", computer_decision)

            elif computer_decision == "Paper":
                print("You lose!", computer_decision, "disproves", player)

            elif computer_decision == "Scissors":
                print("You win!", player, "smashes", computer_decision)

            elif computer_decision == "Lizard":
                print("You lose!", computer_decision, "poisons", player)

                print("Would you like to play again? \n")
                answer = input()

            if answer.lower() == "y" or answer.lower() == "yes":
                game == True
            else:
                break