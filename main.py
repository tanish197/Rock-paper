import random

point_user = 0
point_computer = 0
rounds_played = 0
second_user = False

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "draw"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "paper" and choice2 == "rock") or \
         (choice1 == "scissors" and choice2 == "paper"):
        return "user"
    else:
        return "computer"

while True:
    if rounds_played % 3 == 0:
        second_user_input = input("Do you want to play as a second user? (y/n): ")
        if second_user_input.lower() == "y":
            second_user = True
        else:
            second_user = False
    
    if second_user:
        user_input_1 = input("Second user, enter your choice (rock, paper, scissors): ")
        user_input_2 = input("Enter your choice (rock, paper, scissors): ")
        
        result = determine_winner(user_input_1, user_input_2)
        
        if result == "draw":
            print("It's a draw!")
        elif result == "user":
            print("Second user wins!")
            point_user += 1
        else:
            print("First user wins!")
            point_computer += 1
    else:
        user_input = input("Enter your choice (rock, paper, scissors): ")
        possible_choices = ["rock", "paper", "scissors"]
        computer_input = random.choice(possible_choices)

        print(f"You chose {user_input}, computer chose {computer_input}")

        if user_input in possible_choices:
            result = determine_winner(user_input, computer_input)

            if result == "draw":
                print(f"It's a draw as both selected {user_input}")
            elif result == "user":
                print(f"You win! {user_input} beats {computer_input}.")
                point_user += 1
            else:
                print(f"You lose! {computer_input} beats {user_input}.")
                point_computer += 1
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

    rounds_played += 1

    if rounds_played % 3 == 0:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

print(f"Total Points: User {point_user} - Computer {point_computer}")

if point_user == point_computer:
    print("It's a tie! Nobody won.")
elif point_user > point_computer:
    print("Congratulations! You won!")
else:
    print("Sorry, you lost.")

print("Game Over!")
