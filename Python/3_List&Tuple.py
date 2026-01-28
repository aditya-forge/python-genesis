# Chapter -03 :(List And Tuples)

# LIST ->

# 1. List : NOTE : Build In Data Type 

# Storing Data Into Variable And Printing 

Marks1 = 98.1 
Marks2 = 93.7
Marks3 = 94.6 

print(Marks1)
print(Marks2)
print(Marks3)


# NOTE : Storing This Much Value In Different Variable , Manages More Size / Space Complaxity . For That We Use List .

Marks = [98.1,93.7,94.6]
print(Marks)


# NOTE : We Also Store Different Data Values In Single List 

Marks = ["Aditya",98,9.22]
print(Marks) 


# NOTE : We Can Also Print Data From Specific Location 

Marks = ["Aditya",98,9.22]
print(Marks[1]) 


# 2 . List Slicing : NOTE : Same As String Sliceing -> It Can Print From Specific Index Location To Specific Location From Indexes 

List_Name  = ["list1",23,45.9,"Kanpur"]
print(List_Name[1:len(List_Name)])   #len(list_name) mean Take Last Index
print(List_Name[:3])   #Un Written Auto Take First
print(List_Name[1:])  #From One To Last We Wont entered Any Thing So Take last 
print(List_Name[-4:-1]) # n-1 to -1 indexes 


# [23, 45.9, 'Kanpur']
# ['list1', 23, 45.9]
# [23, 45.9, 'Kanpur']
# ['list1', 23, 45.9]


# 3. Methords In List :  #NOTE : In Build Function Used To Perform Diret Operation . 

'''
1. list.append()
2. list.sort()
3. list.sort(reverse = True)
4. list.reverse() 
5. list.index(indx,value)
6. list.remove()
7. list.pop()
8. list.copy()

'''

# Examples : 


# 1. list.append()

list1 = [1,"Aditya",34.2,897,"Kanpur"]
print(list1.append(30))
print(list1) 


# 2. list.sort()

list1 = [5,4,7,8,2,4,2,1]
list1.sort()
print(list1) 


# 3. list.sort(reverse = True)

list1 = [5,4,7,8,2,4,2,1]
list1.sort(reverse=True)
print(list1) 


# 4. list.reverse() 

list1 = [5,"Aditya",7,8,2,4,2,1]
list1.reverse()
print(list1) 


# 5. list.index(indx,value) : 

list1 = [5,"Aditya",7,8,2,4,2,1]
list1.insert(2,"Sachin")
print(list1) 


# 6. list.remove()

list1 = [5,"Aditya",7,8,2,4,2,1]
list1.remove(2)
print(list1) 


# 7. list.pop()

list1 = [5,"Aditya",7,8,2,4,2,1]
list1.pop(2)  #NOTE Remove From Index Location 
print(list1)


# 8. list.copy()


list1 = [5,"Aditya",7,8,2,4,2,1]
list2 = list1.copy()
print(list2)


# TUPLES -> 

# 1. Tuples : It Is Also An Build In Daattype As List (Inmutable , Odered , Duplicate Entry Valid)

tup = (1,"Aditya",12.8,"Kanpur")
print(tup)
print(tup[1])


tup = (1,)  #NOTE For Single Value If We Remove Comma It Will Take Integer
print(tup)


# 2. Tuple Slicing : NOTE Similar As List , String 

tup  = ("tu1",23,45.9,"Kanpur")
print(tup[1:len(tup)])   #len(list_name) mean Take Last Index
print(tup[:3])   #Un Written Auto Take First
print(tup[1:])  #From One To Last We Wont entered Any Thing So Take last 
print(tup[-4:-1]) # n-1 to -1 indexes 


# 3. Methords In Tuple : 

'''
1. Index(Value) -> Give Index Val Of Given Value in ()
2. Count(Value) -> Count Specific Val In Tuple 
'''

#Example : 

# 1. Index(Value) :

tup  = ("tu1",23,45.9,"Kanpur")
print(tup.index("tu1")) #NOTE Here As String In Print It Print As List Not Give None 


# 2. Count(Value) : 

tup  = ("tu1",23,45.9,"Kanpur",23)
print(tup.count(23))

