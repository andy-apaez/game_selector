import random

name = input("what is your name? ")
print("Hello, " + name + "!")

game = input("what game would you like to play? (colors/numbers) ").lower()

while game not in ["colors", "numbers"]:
    game = input(
        "Invalid choice. Please choose 'colors' or 'numbers': ").lower()


if game == "colors":
    computer_choice = random.choice(["red", "blue", "green", "yellow"])
    user_choice = input("choose a color (red/blue/green/yellow): ").lower()
    if user_choice == computer_choice:
        print(f"wow you got it right {name}!")
    else:
        print(f"Sorry, the correct color was {computer_choice}.")
    exit()

elif game == "numbers":
    computer_choice = random.randint(1, 10)
    user_choice = int(input("choose a number between 1 and 10: "))
    if user_choice == computer_choice:
        print(f"wow you got it right {name}!")
    else:
        print(f"Sorry, the correct number was {computer_choice}.")
    exit()
