num1=input("enter the first number")
while not num1.replace('.','',1).isdigit():
    print("Invalid input. Please enter a number.")
    num1=input("enter the first number")
num1=float(num1)

num2=input("enter the second number")
while not num2.replace('.','',1).isdigit():
    print("Invalid input. Please enter a number.")
    num2=input("enter the second number")
num2=float(num2)

addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
if num2==0:
    division="undefined (division by zero)"
else:
    division=num1/num2

print("result")
print(f"addition:{num1}+{num2}={addition}")
print(f"subtraction:{num1}-{num2}={subtraction}")
print(f"multiplication:{num1}*{num2}={multiplication}")
print(f"division:{num1}/{num2}={division}")
