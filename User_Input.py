def operation_choice():
    print("Please choose an operation:")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Modulus")



    while True:
        choice = input("Please choose an operation(1/2/3/4/5): ")
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
             print("Invalid input. please enter a valid number.")


def number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. please enter a valid number.")