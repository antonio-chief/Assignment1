def add(num1, num2):
      return num1 + num2

def subtract(num1, num2):
      return num1 - num2

def multiply(num1, num2):
      return num1 * num2

def divide(num1, num2):
      return num1 / num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter operation (1/2/3/4): ")
if operation == '1':
      print("Result: ", add(num1, num2))
elif operation == '2':
      print("Result: ", subtract(num1, num2))
elif operation == '3':
      print("Result: ", multiply(num1, num2))
elif operation == '4':
      print("Result: ", divide(num1, num2))
else:
      print("Invalid operation")
