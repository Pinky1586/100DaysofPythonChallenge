def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

import art
print(art.logo)

#Usindg Dictionary to call the functions:
def calculator():
    for key in operations:
        print(key)
    num1 = float(input(f"What is the first number?: "))

    should_continue = True

    while should_continue:
        action = input(f"Pick and operation: ")
        num2 = float(input(f"What is the second number?: "))
        result = float((operations[action](num1, num2)))
        print(f"{num1} {action} {num2} = {result}")

        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if cont == 'y':
            num1 = result
        else:
            should_continue = False
            print(f"Glad I could help. Goodbye.")
calculator()



