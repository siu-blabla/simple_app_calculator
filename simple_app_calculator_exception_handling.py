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
            choice = int(input("\033[1mPlease enter the operation you want to use (1/2/3/4): \033[0m"))
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
            print("\033[91mValue Error: Invalid input! Please enter a valid number\033[0m.")

# Ask user to enter the second number
    while True:
        try:
            num_2 = float(input("Please enter the second number: "))
            if choice == 4 and num_2 == 0:
                print("\033[91mDivision Error: Division by zero is not allowed.\033[0m")
                continue
            break
        except ValueError:
            print("\033[91mValue Error: Invalid input! Please enter a valid number.\033[0m")

# Execute the chosen math operation and display the output
    try:
        if choice == 1:
            solution = num_1 + num_2
            print(f"\033[92mThe sum is: \033[1m{int(solution) if solution.is_integer() else solution}\033[0m")
        elif choice == 2:
            solution = num_1 - num_2
            print(f"\033[31mThe difference is: \033[1m{int(solution) if solution.is_integer() else solution}\033[0m")
        elif choice == 3:
            solution = num_1 * num_2
            print(f"\033[94mThe product is: \033[1m{int(solution) if solution.is_integer() else solution}\033[0m")
        elif choice == 4:
            solution = num_1 / num_2
            print(f"\033[95mThe quotient is: \033[1m{int(solution) if solution.is_integer() else solution}\033[0m")

    except ZeroDivisionError:
        print("\033[91mDivision Error: Division by zero is not allowed.\033[0m")
    except Exception as exception:
        print("\033[91mAn unexpected error occurred:\033[0m", exception)

# Looping (Ask user if they want to try again)
