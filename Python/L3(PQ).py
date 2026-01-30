# 1. WAP To Ask User To Enter Name Of Their Three Favorite Movie And Store It Into List 

fav_Movie = input("Enter Three Favorite Movie : ").split()
print(fav_Movie)
print(type(fav_Movie))


# 2. WAP To Check If A List Contains Palindrome of Element (Hint Use Copy() Methord )

element = input("Enter Element : ").split()
print(element)
element2 = element.copy()
element2.reverse()

if(element == element2):
print("List Is Palindome")
else:
print("List Is Not Palindome")


# 3. WAP to count the number of students with the “A” grade in the following tuple.
# "C","D","A","A","B","B","A"
# Store the above values in a list & sort them from “A” to “D”.

  
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))
list1 = list(tup).copy()
list1.sort()
print(list1)
