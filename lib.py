import random

print("Welcome to the rock, paper, and scissors game!!")

# Define ASCII art drawings
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Take player input and convert it to lowercase
player_choice = input("ROCK, PAPER, or SCISSORS? ").lower()

# Generate random choice for computer
options = ['rock', 'paper', 'scissors']
pc_choice = random.choice(options)

print("\nPlayer chose:")
# Display ASCII art for player's choice
if player_choice == 'rock':
    print(rock)
elif player_choice == 'paper':
    print(paper)
elif player_choice == 'scissors':
    print(scissors)

print("\nComputer chose:")
# Display ASCII art for computer's choice
if pc_choice == 'rock':
    print(rock)
elif pc_choice == 'paper':
    print(paper)
elif pc_choice == 'scissors':
    print(scissors)

# Define the game rules
rules = {
    'rock': {'beats': 'scissors', 'loses to': 'paper'},
    'paper': {'beats': 'rock', 'loses to': 'scissors'},
    'scissors': {'beats': 'paper', 'loses to': 'rock'}
}

# Compare player and computer choices and determine the winner
if player_choice == pc_choice:
    print("\nIt's a draw!")
elif rules[player_choice]['beats'] == pc_choice:
    print("\nYou win!")
else:
    print("\nYou lose!")
