
print("*** Phyton Calculator Program ***")
operator = input("Enter an operator(+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
def add(value1, value2):
    return value1 + value2
def substraction (value1, value2):
    return value1 - value2
def multiply (value1, value2):
    return value1 * value2
def divide (value1, value2):
    return value1 / value2

if operator == '+':
    result = add(num1, num2)
    print(f"Calculated result: {num1} + {num2} = {round(result, 2)}")
elif operator == '-':
    result = substraction(num1, num2)
    print(f"Calculated result: {num1} - {num2} = {round(result, 2)}")
elif operator == '*':
    result = multiply(num1, num2)
    print(f"Calculated result: {num1} * {num2} = {round(result, 2)}")
elif operator == '/':
    result = divide(num1, num2)
    print(f"Calculated result: {num1} / {num2} = {round(result, 2)}")
else:
   print(f"{operator} is not a valid operator. Please try again.")
