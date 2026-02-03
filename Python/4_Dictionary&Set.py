# Chapter - 04 ( Dictionary & Set's )

# 1) Dictionary : It Is An In Build Datatype Used In Python (Unodered,Mutable,Duplicate Entry Not Allowed,Multiple Data Value Allowed ) , Collection Of Data In Key : Value Pair Where Key And Value In Any Data Set As Key & Any As Value .  

# NOTE : Their Will Be Only One Key As Same In Dictionary Duplicate Entry Not Allowd But Their Possible Value May Be Having Multiple . 


# Example : Syntax :
 
#Here We Will Discuess Any Sort Of Info In Any Combination 

disct = {
    "name" : "Aditya",
    "Id" : 333,
    "Sem" : 4 ,
    "College" : "SRM AP",
    "Subjects" : ["DBMS","Python","Probability","Coding Skills","Full Stack","Soft Skill"],
    2 : "Sachin",
    2.1 : "Alok"
}


#Acess Data Value From Dictionary : 

print(disct["name"])   #Acess Element

print(disct["Subjects"][2]) # Printing Probability List In Subject 

disct["name"] = "Aryan Manhas"  #Updation In Dictionary Possible As We Know
print(disct["name"])

disct["Branch"] = "CSE" #Adding New Key Value Pair Into Disctionary , WeCan Add Any Sort Of Data Set 
print(disct)  #After Printing We Noticed At The Lat Of Dictionary This Key Value Pair Is Added


# Creating Empty List And Adding Some Value Into  It : 

info = {} # Empty list
print(info) 


#Input Or Updating Values In Empty List  : 

info["name"] = "Aditya Kumar" , "Sachin Kumar"
print(info)  #Print Updated Dictionary 


# Nested Dictionary : 

# Whean We  Will Add Another Dictionary In An Key In Previous Disct Then We Will Say That It Is Nested  Dictionary 

nested_disct = {
    "Name" : "Aditya Kumar",
    "College": "SRM AP",
    "Course" : "Btech CSE",
    "Semester" : 4 ,
    "Sub_Marks" : {
        "DBMS" : 99,     #Nested Dictionary
        "Full Stack" : 98
    },
    "Cgpa" : 9.22
}


print(nested_disct["Sub_Marks"]["DBMS"])  # This Is How We Acess In Nested Dictionary 

nested_disct = {
    "Add" : 23
} 

print(nested_disct)


# Methord Used In Disctionary :

'''

1. disct.keys()  # Give All The Keys Present In Dictionary
2. disct.values() # Give All The Values Present In Dictionary
3. disct.item() # Give All Of The Key Values In Tuple
4. disct.get() # It Will Acess Without Throuing Error return value 
5. disct.update() # It Is Used To Update Any Dictionary
6. disct.copy() # Copy The Dictionary In Another Dictionary 
7. disct.pop()
8. disct.popitem()
9. disct.setdefault()
10. clear() #Remove All The Element Of Dictionary

'''


#Example Of Main Methords : 

classbtech = {
    "Name" : "Aditya Kumar",
    "Standard" : "BTECH",
    "Subject" : {
        "DBMS" : 100,
        "Maths" : 99,
        "Python" : 98
    }
}

print(classbtech.keys())


print(classbtech.values())


print(classbtech.items())


print(classbtech.get("Subject"))


new_class = {
    "Name" : "AdityaT"
}
print(classbtech.update(new_class))  #In This Limne It Through None Not Any Output Case
print(classbtech)

#or 

classbtech.update({"City" : "Kanpur"})
print(classbtech)


#Sets : 

set1 = { 1 , 2 , 3 , 4 , "SRM "}
print(set1)

list1 = set()
print(list1)


set2 = set()

print(set2.add(3))
print(set2)


sett = { 1, 2 , 3, 4 ,5 , "Aditya" , 9.22}
sett.clear()
print(sett)


def  fun():
    pass
print(fun())