import re

def validate_num(number_string):
    if not number_string: 
        return False
    any_number_pattern = r"^[+-]?(\d*\.\d+|\d+)$"
    return re.match(any_number_pattern, number_string) is not None

# Arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("float division by zero")
        return None
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("float division by zero")
        return None
    return a % b

# Operation selection
def select_op(choice):
    if choice == '#':
        print("Done. Terminating")
        return -1 
    elif choice == '$':
        return 0  
    elif choice not in ['+', '-', '*', '/', '^', '%']:
        print("Unrecognized operation")
        return 0

    # Get first number
    while True:
        num1 = input("Enter first number: ")
        print(num1)
        if '$' in num1:
            return 0
        elif num1 == '#':
            print("Done. Terminating")
            return -1
        if validate_num(num1):
            break
        print("Not a valid number,please enter again")
    
    # Get second number
    while True:
        num2 = input("Enter second number: ")
        print(num2)
        if '$' in num2:
            return 0
        elif num2 == '#':
            print("Done. Terminating")
            return -1
        if validate_num(num2):
            break
        print("Not a valid number,please enter again")

    try:
        num1 = float(num1)
        num2 = float(num2)

        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)

        if result is not None:
            print(f"{num1:.1f} {choice} {num2:.1f} = {result:.1f}")
        else:
            print(f"{num1:.1f} {choice} {num2:.1f} = None")
    except ValueError:
        print("Not a valid number,please enter again")
        return 0
    except Exception:
        print("Something Went Wrong")
        print(f"{num1:.1f} {choice} {num2:.1f} = None")
        return 0

    return 0

# Main loop
while True:
    print("Select operation.")
    print("1.Add      : +")
    print("2.Subtract : -")
    print("3.Multiply : *")
    print("4.Divide   : /")
    print("5.Power    : ^")
    print("6.Remainder: %")
    print("7.Terminate: #")
    print("8.Reset    : $")
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice) 
    if select_op(choice) == -1:
        break


# End of the demo.py file
print("Exiting the calculator. Goodbye!")