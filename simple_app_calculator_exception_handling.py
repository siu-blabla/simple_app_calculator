# Introduction
print("\033[93m\033[1m----------------THIS IS A SIMPLE CALCULATOR APP----------------")
print()

# Display Options
print("Please choose your desired math operation: \033[0m")
print("\033[92m1. Addition \033[0m")
print("\033[31m2. Subtraction \033[0m")
print("\033[94m3. Multiplication \033[0m")
print("\033[95m4. Division \033[0m")
print()

# Ask the user to choose their desired math operation
while True:         # Loop command for the whole program's loop function
    while True:
        try:
            choice = int(input("\033[1mPlease enter the operation you want to use (1/2/3/4): \033[1m"))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("\033[91m\033[4mInvalid input! Please enter a number between 1 to 4 only.\n\033[0m")
        except ValueError:
            print("\033[91m\033[4mInvalid input! Please enter a valid number.\033[0m")

# Ask user to enter the first number
    while True:
        try:
            num_1 = float(input("Please enter the first number: "))
            break
        except ValueError:
            print("\033[91mValueError: Invalid input! Please enter a valid number\033[0m.")

# Ask user to enter the second number
# Execute the chosen math operation and display the output
# Looping (Ask user if they want to try again)
