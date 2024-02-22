# main.py

from utils.random_generator import generate_random_number
from utils.input_validator import validate_input

def guess_the_number():
    secret_number = generate_random_number()
    attempts = 0

    while True:
        user_guess = validate_input("Guess the number (between 1 and 100): ")
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    guess_the_number()
