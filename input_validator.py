# input_validator.py

def validate_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if 1 <= user_input <= 100:
                return user_input
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")
