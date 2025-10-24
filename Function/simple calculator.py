def calculator(num1, num2, op):
    
    if op == '+':
        print("add",num1 + num2)
    elif op == '-':
        print("sub",num1 - num2)
    elif op == '*':
        print("mul",num1 * num2)
    elif op == '/':
        print("div",num1 / num2)
    else:
        print("Invalid operation")
        
calculator(3, 4, '+')
calculator(5, 4, '-')
calculator(10, 5, '*')
calculator(5, 10, '/')
