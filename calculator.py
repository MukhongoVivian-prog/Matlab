# Function to perform calculations without return statements
def calculate(num1, num2, operation):
    if operation == '+':
        print("Result:", num1 + num2)
    elif operation == '-':
        print("Result:", num1 - num2)
    elif operation == '*':
        print("Result:", num1 * num2)
    elif operation == "%":
        print("Result:", num1 % num2)
    elif operation == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operation")

print("Enjoy working with our Simple Calculator Program!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, %): ")

calculate(num1, num2, operation)

print("Thank you for trying this out with Group ONE!")
