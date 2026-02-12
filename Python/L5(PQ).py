#Practice Set :  5 


#Print Value From 1 to 100
i = 1 
while i <= 100 : 
print(i)
i+=1 


#Print Value From 100 to 1
i = 100 
while i >= 1 : 
print(i)
i-=1 


#Multiplication Table 
i = 1 
n = int(input("Enter n : "))
while i<=10:
print(n, "x" , i ,"=" , n*i)
i +=1 


#Print Value Of list
num = [1,4,9,16,25,36,49,64,81,100]
index = 0 
while index < len(num) :
print(num[index])
index+=1
   

#Search Value Of List
x = int(input("Key : "))
num = [1,4,9,16,25,36,49,64,81,100]
index = 0 
while index < len(num) :
if(num[index] == x):
print("Element Found As : " , x )
index+=1


#Print Value Of List
num = [1,4,9,16,25,36,49,64,81,100]
for x in num : 
print(x)


#Search Value In Tuple
x = int(input("Key : "))
num = (1,4,9,16,25,36,49,64,81,100)
for y in num : 
if(y == x):
print(x," Is Found")
#         break
else: 
print("Not Found")


#Print Value From 1 to 100
for i in range(1,101):
print(i)


#Print Value From 100 to 1
for i in range(100,0,-1):
print(i)


#Multiplication Table Of A Number : 
n = int(input("n : "))
for i in range(1,11):
print(n,'x',i , n*i)


# WAP To Find The Sum Of First n Number Using While Loop 
n = int(input("Enter Nth number :"))
i = 0
sum = 0
while i<= n : 
sum += i 
i+=1 
print(sum)


#WAP To Find Factorial Of First N numbers  Using for Loop 

n = int(input())
fact = 1
for i in range (1,n+1,1) :
fact *= i 
print(fact)

