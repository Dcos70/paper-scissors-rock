import random

def get_user_choice():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice please!(rock/paper/scissors): ").lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    valid_choices = ["rock", "paper", "scissors"]
    return random.choice(valid_choices)

def determin_winner(user_choice, computer_choice):

    rules = {
        "rock": ["scissors"],
        "paper": ["rock"],
        "scissors": ["paper"],
    }

    if user_choice == computer_choice:
       return "It's a tie!"
    elif get_computer_choice in rules[user_choice]:
       return "Congrats you win!"
    else:
       return "Computer wins!"
 
def play_game():
    print("Welcome to rock, paper, scissors!, would you like a game?")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        winner = determin_winner(user_choice, computer_choice)
        print(winner)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
           break

play_game() 
