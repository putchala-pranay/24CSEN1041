def calculator(a, b=None, op=None):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:   
            return "Error: Division by zero is not allowed"
        else:
            return a / b
    elif op == 'square':
        return a ** 2
    elif op == 'sqrt':       
        return a ** 0.5
    elif op == 'cube':
        return a ** 3
    elif op == 'binary':
        return bin(a)        
    elif op == 'decimal':
        return int(a)       
    elif op == 'hex':
        return hex(a)       
    else:
        return "Invalid operator"

print("Available operations: +, -, *, /, square, sqrt, cube, binary, decimal, hex")

op = input("Enter operation: ")

if op in ['+', '-', '*', '/']:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", calculator(a, b, op))
else:
    a = int(input("Enter a number: "))
    print("Result:", calculator(a, op=op))
