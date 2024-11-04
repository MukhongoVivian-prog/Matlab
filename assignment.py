# A simple calculator python program that implements user input and output

# Function to perform calculations
def calculate(num1, num2, operation):

    if operation == '+':
        return num1 + num2

    elif operation == '-':
        return num1 - num2
    elif operation == '*':

        return num1 * num2

    elif operation == "%":
        return num1 % num2

    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"


print("Enjoy working with our Simple Calculator Program!")
try:

    num1 = float(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /, %): ")

   
    result = calculate(num1, num2, operation)
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

print("Thank you for trying this out with Group ONE!")