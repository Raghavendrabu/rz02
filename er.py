
#input
full_name=input("enter your full_name")

#validating input:Ensure at least two words are entered
while " "not in full_name:
    print("Error: Please enter at least your first and last name.")
    full_name=input("Enter your full name: ")

#splitting first and last name
print("----\nspliting ")
name_parts=full_name.split()
first_name=name_parts[0]
last_name=name_parts[-1]
print(first_name)
print(last_name)
#Printing extracted names
print("------\nPrinting extarcted names")
print("First Name:",first_name)
print("Last Name:",last_name)

#Reversing order
print("---\nReverses order(Last,First):",last_name,first_name)

#Converting to uppercase and lowercase
print("-----\nUppercase:",full_name.upper())
print("Lowercase:",full_name.lower())

#string
print(f"welcome,{full_name}")
