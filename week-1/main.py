def calculate():
    # A basic calculator program

    print('''
This is a simple calculator program. It can perform 4 operations,
    Addition => +
    Subtraction => -
    Multiplication => *
    Division => /
Provide inputs as required.
press CTRL + C to exit.
        ''')
    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))
    operator = input("Enter desired operation: ")

    valid_operators = ["+", "-", "*", "/"]

    if operator in valid_operators:
        if operator == "+":
            answer = number_1 + number_2
        elif operator == "-":
            answer = number_1 - number_2
        elif operator == "*":
            answer = number_1 * number_2
        elif operator == "/":
            answer = number_1 / number_2
    else:
        print("Enter a valid operation")

    return f"\n{number_1} {operator} {number_2} = {answer}"


if __name__ == "__main__":
    while True:
        print(calculate())
