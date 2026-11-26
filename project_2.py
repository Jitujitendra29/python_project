# Guess the Number game using NumPy in Python (Project -> 2)

import numpy as np

# Generate a random number between 1 and 100 (inclusive)
secret_number = np.random.randint(1, 101)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("I have picked a secret number between 1 and 100. Can you guess it?")

while True:
    try:
        user_guess = int(input("\nEnter your guess (1-100): "))
        attempts += 1

        if user_guess < 1 or user_guess > 100:
            print("⚠️ Please enter a number within 1 to 100.")
            continue

        if user_guess < secret_number:
            print("📉 Too low! Try a higher number.")
        elif user_guess > secret_number:
            print("📈 Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You found the number {secret_number} in {attempts} attempts!")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")

