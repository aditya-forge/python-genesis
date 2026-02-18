# WAP To Write A length Of A List (list is the parameter)

def length_list(list1):
count = 0
for x in list1 :
count+=1
return count

list1 = [1,2,3,4]
m = length_list(list1)
print(m)


def single_line (list2): 
for x in list2:
print(list2)
#         break

t = input("Enter List Val :").split()
# single_line(t) 


def fact(n):
fact = 1
for x in range(1,n+1,1):
fact*=x
return fact

n = int(input("n : "))
m = fact(n)
print(m)


def curr_convert(USD):
INR = USD * 100 
return INR 

print("CURRENCY CONVETOR ")
USD = float(input("USD : "))
x = curr_convert(USD)


def Even_Odd_Check(num):
if(num%2 == 0):
return "Even"
else:
return "ODD"

num = int(input("Num : "))
result = Even_Odd_Check(num)
print(result)


def checkprime(n):
count = 0
for x in range(1,n+1,1):
if (n%x == 0):
count += 1 
if(count<= 2):
return "PRIME NO."
else:
return "NOT PRIME NO."

n = int(input("Enter Num : "))
m = checkprime(n)
print(m)


def sum_el_list(list1):
sum1 = 0
for x in list1 : 
sum1 += x 
return sum

list1 = list(map(int,input("Enter Element In List : ").split()))
m = sum_el_list(list1)
print(m)


def large_el(list1):
print(max(list1))

list1 = list(map(int,input("List val : ").split()))
# large_el(list1)


def large_el(list1):
key = list1[0]
for x in list1 :
if(list1[x] > key ):
key = list[x]
else:
#             pass
return key

list1 = list(map(int,input("List val : ").split()))
m = large_el(list1)
print(m)


def large_el(list1):
key = list1[0]   # assume first element is largest
for x in list1:
if x > key:
key = x
return key

list1 = list(map(int, input("List val : ").split()))
m = large_el(list1)
print(m)


def revstr(str):
return(str[::-1])


str = input()
m = revstr(str)
print(m)


def palnidome(str1):
    if(str1 == str1[::-1]):
        return "YES"
    else:
        return "NO"

str1 = input()
m = palnidome(str1)
print(m)