import random

user_choice = int(input("Enter your choice:Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
comp_choice = random.randint(0,2)
print("Computer choice")
print(comp_choice)
if comp_choice == user_choice:
    print("It's a draw.")
elif comp_choice > user_choice:
    print("You lose.")
elif user_choice > comp_choice:
    print("You win")
elif comp_choice == 0 and user_choice == 2:
    print("You lose.")
elif user_choice == 1 and comp_choice == 2:
    print("You Win.")