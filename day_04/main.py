# the polished Rock-Paper-Scissors game (with error handling)
import random

# ASCII Art for choices (optional)
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
---'   ____)____
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

choices = [rock, paper, scissors]

# Get user input safely
try:
    user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. Please enter 0, 1, or 2.")
    else:
        print("You chose:")
        print(choices[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(choices[computer_choice])

        # Game logic
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")
except ValueError:
    print("Invalid input. Please enter a number (0, 1, or 2).")
