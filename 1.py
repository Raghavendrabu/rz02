w=["i","am","a","student"]
sentence=" ".join(w)
print(sentence)
   
#f-strings
name="raghu"
city="bangalore"
msg=f"my name is {name} and i am from {city}"
print(msg)

#handling numbers in concatenation
name="zoro"
score=100
res=name +" "+ "score" +" "+ str(score)+" " + "points"
print(res)

#displaying flight details
flight="AI 890"
source="BLR"
destination="DEL"
tiket=(f"flight:{flight} \nsource:{source} \ndestination:{destination}")
print(tiket)

#format
name="raghu"
age=23
uid=1234
msg="my name is {} and i am {} years old. my uid is {}".format(name,age,uid)
print(msg)

a="raghu"
b=23
s="{0} is {1} years old".format(a,b)
print(s)

#named arguments
msg="my name is {name} and i am {age} years old".format(name="raghu",age=23)
print(msg)

#formating numbers (decimals and currency)
price=497.879
formmated_price="the price is ${:.2f}".format(price)
print(formmated_price)

#aligning text for reports and tables
print("product:{:<10} price:{:<8}.".format("laptop",55000))
print("product:{:<10} price:{:<8}.".format("phone",35000))


#string slicing
text="bengaluru"
print(text[0:3])
print(text[1:5])

#omiting start or end index
text="badami"
print(text[0:])
print(text[:5])

#negative indexing
text="badami"
print(text[-6:])
print(text[:-1])


#slicing with step
text="bengalore"
print(text[0:6:1])