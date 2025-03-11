import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose: {player}, Computer choose: {computer}")

    if player == computer:
        return "It's a tie!"
    else:
        if player == "rock" and computer == "scissors" or player == "paper" and computer == "rock" or player == "scissors" and computer == "paper":
            return "Player win!"
        else:
            return "Computer win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)

# print("Hello World!")