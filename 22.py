# This program performs basic arithmetic operations on two numbers provided by the user.
num1=input("Enter first number: ")
while not num1.replace(".","").isdigit():
    print("Invalid input. Please enter a number.")
    num1=input("Enter first number: ")
num1=float(num1)

# Convert the input to a float
num2=input("Enter second number: ")
while not num2.replace(".","").isdigit():
    print("Invalid input. Please enter a number.")
    num2=input("Enter second number: ")
num2=float(num2)

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2==0:
    division = "undefined (division by zero)"
else:
    division = num1 / num2
    print("result")
    print(f"addition:{num1}+{num2}={addition}")
    print(f"subtraction:{num1}-{num2}={subtraction}") 
    print(f"multiplication:{num1}*{num2}={multiplication}")
    print(f"division:{num1}/{num2}={division}")


