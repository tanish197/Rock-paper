import random

point_user = 0
point_computer = 0
rounds_played = 0

while True:
    user_input = input("Enter your choice (rock, paper, scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_input = random.choice(possible_choices)

    print(f"You chose {user_input}, computer chose {computer_input}")

    if user_input == computer_input:
        print(f"It's a draw as both selected {user_input}")
    elif user_input == "rock":
        if computer_input == "scissors":
            print(f"You win! Rock will break the scissors.")
            point_user += 1
        else:
            print(f"You lose! Paper will cover the Rock.")
            point_computer += 1
    elif user_input == "paper":
        if computer_input == "rock":
            print(f"You win! Paper will cover the rock.")
            point_user += 1
        else:
            print(f"You lose! Scissors will cut the paper.")
            point_computer += 1
    elif user_input == "scissors":
        if computer_input == "paper":
            print(f"You win! Scissors will cut the paper.")
            point_user += 1
        else:
            print(f"You lose! Rock will break the scissors.")
            point_computer += 1

    rounds_played += 1

    if rounds_played >= 3:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break
        rounds_played = 0

print(f"Total Points: User {point_user} - Computer {point_computer}")

if point_user == point_computer:
    print("It's a tie! Nobody won.")
elif point_user > point_computer:
    print("Congratulations! You won!")
else:
    print("Sorry, you lost.")

print("Game Over!")
