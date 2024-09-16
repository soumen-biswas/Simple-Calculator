def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error! Division by zero!"

def modulus(num1, num2):
    try:
        return num1 % num2
    except ZeroDivisionError:
        return "Error! Division by zero!"