from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float( input("What's the first number: "))

    for symbol in operations:
        print(symbol)
        
    end_calc = False
            

    while not end_calc:
        operation_symbol = input("Pick an operation: ")
        num2 = float( input("What's the next number: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        
        if continue_calc == 'y':
            num1 = answer
        else:
            end_calc = True
            # Recursion => pada dasarnya adalah gagasan bahwa anda dapat memiliki fungsi yg memanggil dirinya sendiri.
            calculator()
            
calculator()