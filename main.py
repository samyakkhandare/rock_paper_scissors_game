import random

"""
rock = 1
paper = -1
scissors = 0
"""

# Correct dictionaries
yourDict = {"rock": 1, "paper": -1, "scissors": 0}
reversedDict = {1: "rock", -1: "paper", 0: "scissors"}

# Get computer choice
computer = random.choice([-1, 0, 1])

# Get user input
youstr = input("Enter your choice (rock/paper/scissors): ").lower()

# Check for valid input
if youstr not in yourDict:
    print("Invalid input!")
else:
    you = yourDict[youstr]

    # Show choices
    print(f"You chose: {reversedDict[you]}")
    print(f"Computer chose: {reversedDict[computer]}")

    # Determine result
    if computer == you:
        print("It's a draw!")
    elif (you == 1 and computer == 0) or (you == 0 and computer == -1) or (you == -1 and computer == 1):
        print("You win!")
    else:
        print("You lose!")

        
        