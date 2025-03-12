import random
import unittest

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
print("\nUNIT TEST")
class WinnerResultTestCase(unittest.TestCase):
    # Tie result
    def test_tie_result(self):
        print('\nTie Result:')
        self.assertEqual(check_win('rock', 'rock'), "It's a tie!")
        self.assertEqual(check_win('paper', 'paper'), "It's a tie!")
        self.assertEqual(check_win('scissors', 'scissors'), "It's a tie!")

    # Player win result
    def test_player_win_result(self):
        print('\nPlayer Win Result:')
        self.assertEqual(check_win('rock', 'scissors'), "Player win!")
        self.assertEqual(check_win('paper', 'rock'), "Player win!")
        self.assertEqual(check_win('scissors', 'paper'), "Player win!")

    # Computer win result
    def test_computer_win_result(self):
        print('Computer Win Result:')
        self.assertEqual(check_win('rock', 'paper'), "Computer win!")
        self.assertEqual(check_win('paper', 'scissors'), "Computer win!")
        self.assertEqual(check_win('scissors', 'rock'), "Computer win!")

if __name__ == '__main__':
    unittest.main()