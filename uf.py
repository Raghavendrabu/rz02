m = float(input("Enter marks: "))
if 9 <= m <= 10:
    print("O")
elif (8 <= m < 9):
    print("A+")
elif 7 <= m < 8:
    print("A")
elif 6 <= m < 7:
    print("B+")
elif 5 <= m < 6:
    print("B")
elif 4 <= m < 5:
    print("C")
elif 3 <= m < 4:
    print("D")
else:
    print("F")