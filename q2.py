import random

# Start
print("Welcome to the Number Guessing Game!")

# Define the number range
num_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Select a random number from the range
secret_num = random.choice(num_range)

# Loop until the correct guess
while True:
    # Prompt user for input
    try:
        guess_num = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check guess
    if guess_num == secret_num:
        print("Congratulations, your guess is correct!")
        break
    elif guess_num < secret_num:
        print("Your guess is too low, try again.")
    elif guess_num > secret_num:
        print("Your guess is too high, try again.")