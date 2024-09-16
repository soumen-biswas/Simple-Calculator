from User_Input import *
from Function_Definitions import *

def calculator():
    while True:
        choice = operation_choice()

        num1 = number_input("Enter first number: ")
        num2 = number_input("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        elif choice == '5':
            result = modulus(num1, num2)
            operation = '%'

        print(f"{num1} {operation} {num2} = {result}")

        next_calculation = input("Would you like to perform another calculation? (y/n): ")
        if next_calculation.lower() != 'y':
            break


calculator()