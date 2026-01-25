#Write A Program To Input Users First Name & Print Length

str = input("Enter First Name : ")
print(len(str))


#WAP To Find Occurrence Of $ In a String 

str = "This $ Is So Expensive But In Compare To Rupee and $ is used In Internatinal Market"
print(str.count("$"))


# Grade Student Based On Mark : 

Marks = int(input("Marks : "))
if(Marks>=90):
print("A")
elif(Marks<90 and Marks >=80):
print("B")
elif(Marks<80 and Marks >=70):
print("C")
elif(Marks<70):
print("D")
else:
print("Wrong Input!")
print("Grade Generated Accoding To Marks")


#WAP To Check If a Number Entered By User Is Odd Or Even 

Number = int(input("Enter Number : "))
if(Number%2 == 0):
print("Even Number")
else:
print("Odd Number")


# WAP To Find Greatest Of 3 Num Enter By User 

Number1 = int(input("Enter Number1 : "))
Number2 = int(input("Enter Number2 : "))
Number3 = int(input("Enter Number3 : "))
if(Number1>=Number2 and Number1>=Number3 ):
print("Number1 Is Greatest As ",Number1)
elif(Number2>=Number3 ):
print("Number2 Is Greatest As ",Number2)
else:
print("Number3 Is Greatest As ",Number3)


# WAP To Check Chaeter The Number Is Multiple Of 7 or Not 

num = int(input("Num :"))
if(num%7 == 0):
print("Multiple Of 7 As :",num)
else:
print("Not Multiple Of 7 As :",num)


