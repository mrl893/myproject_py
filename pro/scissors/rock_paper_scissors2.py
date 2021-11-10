import random

OPTIONS = ["rock", "paper","scissors"]
# print("(1) Rock\n(2) Paper\n(3) Scissors")

def get_computer_choice():
    return random.choice(OPTIONS)

def get_humman_choice():
    choice_number = int(input("Enter the number of your choice:  "))
    return OPTIONS[choice_number - 1]

def print_options():
    print("\n".join(f"({i}) {options.title()}" for i,
    options in enumerate(OPTIONS)))


def print_choice(human_choice, computer_choice):
    print(f"You chose {human_choice}")
    print(f"The computer chose {computer_choice}")


def print_win_lose(human_choice, computer_choice, human_beats,human_loses_to):
    if computer_choice == human_loses_to:
        print(f"Sorry, {computer_choice} beats {human_choice}")
    elif computer_choice == human_beats:
        print(f"Yes, {human_choice} beats {computer_choice}!")

def print_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        print("Draw!")

    if human_choice == "rock":
        print_win_lose("rock", computer_choice, "scissors", "paper")
    elif human_choice == "paper":
        print_win_lose("paper", computer_choice, "rock", "scissors")
    elif human_choice == "scissors":
        print_win_lose("scissors", computer_choice, "paper", "rock")

print_options()
human_choice = get_humman_choice()
computer_choice = get_computer_choice()
print_choice(human_choice, computer_choice)
print_result(human_choice, computer_choice)
