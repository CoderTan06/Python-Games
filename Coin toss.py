#Coin toss simulator program - TS
import random

print("Welcome to the Coin Toss Simulator!")

while True:
    user_input = input("Enter 't' to toss the coin or 'q' to quit: ").lower()

    if user_input == 't':
        result = random.choice(["Heads", "Tails"])
        print("The coin shows:", result)
    elif user_input == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 't' or 'q'.")
#End of program
