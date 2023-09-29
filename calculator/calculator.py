CHOICES = ["add", "subtract", "multiply", "divide", "remainder"]

def display_operators():
    print(f"Valid operators: {', '.join(CHOICES)}")

def get_operator():
    while True:
        choice = input("Enter operation: ").lower()
        if choice in CHOICES:
            return choice
        print("Invalid operation!")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def remainder(num1, num2):
    return num1 % num2

def get_operands():
    operands = []
    for i in range(2):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
            except ValueError:
                print("Invalid number!")
            else:
                operands.append(num)
                break

    return (*operands,)

def display(num1, num2, operator, result):
    print(f"{num1} {operator} {num2} = {result}")

def main():
    display_operators()
    operator = get_operator()
    operands = get_operands()
    symbol = ""

    process = None
    if operator == "add":
        process = add
        symbol = "+"
    elif operator == "subtract":
        process = subtract
        symbol = "-"   
    elif operator == "multiply":
        process = multiply
        symbol = "*"
    elif operator == "divide":
        process = divide
        symbol = "/"
    else:
        process = remainder
        symbol = "%"

    result = process(*operands)
    display(*operands, symbol, result)

if __name__ == "__main__":
    main()
