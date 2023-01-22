import random

print("Welcome to Rock-Paper-Scissors!")

while True:
    # Get the player's choice
    player = input("Enter rock, paper, or scissors: ").lower()

    # Check if the player's choice is valid
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        continue

    # Get the computer's choice
    computer = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        break
