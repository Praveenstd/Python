import math

while True:
    print("\nAvailable Operators: +, -, *, /, %, ^, sqrt, !")
    
    while True:
        operator = input("Enter the Operator: ")
        if operator in ['+', '-', '*', '/', '%', '^', 'sqrt', '!']:
            break
        print("Invalid operator. Please enter a valid one.")

    if operator in ['+', '-', '*', '/', '%', '^']:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed")
                continue
            result = num1 / num2
        elif operator == '%':
            result = num1 % num2
        elif operator == '^':
            result = num1 ** num2

    elif operator == 'sqrt':
        num = float(input('Enter the number: '))
        if num < 0:
            print("Error: Cannot find square root of a negative number")
            continue
        result = math.sqrt(num)

    elif operator == '!':
        num = int(input('Enter a non-negative integer: '))
        if num < 0:
            print("Error: Factorial is not defined for negative numbers")
            continue
        result = math.factorial(num)

    print("Result:", result)

    again = input("Wanna continue calculating? (y/n): ").lower()
    if again == 'n':
        break
print("Thanks For using my calculator")