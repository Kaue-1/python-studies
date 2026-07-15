operator = input("Enter an operator (+ - * /): ")
valid_operators = "+", "-", "*", "/"

while operator not in (valid_operators):
    print(f"{operator} is not a valid operator")
    operator = input("Please enter only aritmetcs operators (+, -, *, /): ").strip()
    

num1 = float(input("Enter de first number:"))
num2 = float(input("Enter de second number:"))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))