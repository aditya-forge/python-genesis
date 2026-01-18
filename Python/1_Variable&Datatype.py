# Chapter 1 : (Variable , Datatypes And Operator) 


# First Program :

print("Hello World")

#Here It Will Print Both Sentence In Single Line
print("My Name Is Aditya","My Age Is 20")

print(20) ##Here It Will Print 20
print(20+30) ##Here It Will Give Print Addition Of Both


# Variable :


name = "Aditya"
age = "20" # " " or ' ' or ''' '''

print(name) # For Printing This We Can Not UsE Double Quotes
print(age)

#If We Want To Write An Type Of The Respective Variable we Can Easily Do 
#In Python It By Deafault Using The Value Get Their Variable Value And Using type() Fun We Can Analyse Also

name ="Aditya" # Here Equal To Shows Right Side Value Is Coping To Left Side 
age = 20
cgpa = 9.22
print(type(name))
print(type(age))
print(type(cgpa))


# Data Type 


# Integer  : It Will Use Direct Writting In () includes All Integer Values
# Float :  It Will Take All Real Values Having 4 bit
# String : It Will Write in " " or ' ' or ''' ''' Combination Of Letter
# Bolean : It Either Give Result In True or False
# None : Empty

a = 2
b = 2.22
c = "Aditya"
d = True 
e = None 
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


#WAP To Find Sum Of A Num As Print  


a = 2 
b = 3
c = a+b  # Any Operation We Want To Perform We Wrote At  The Place Of +
print(c)


# Comment In Python 


#For Single Line : 

# use # 

#For Multiple line as :

#''' Multiple
#  line'''


#10 Types Of Operators : 

'''
1. Arthematic Operator (+,-,*,/,%,**)
2. Relational/Conditional Operator (==,!=,<,<=,>,>=)
3. Assignment Operator (=,+=,-+,*=,%=,/=,**=)
4. Logical Operator (and , or , not)
'''

#Example : 


#1. Arthematic Operator : 

a=20
b=30

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)


#2. Relational Operator : #NOTE Give Output In Term Of If True Or False If Conditional Applied Or In Direct Print Give True Or False 

a=20
b=30

print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)


#3. Assigenement Operator :   NOTE : We cant exicute this in Print 

''' 

a=a+b -> a+=b
a=a-b -> a-=b
a=a*b -> a*=b
a=a/b -> /=b
a=a%b -> a%=b
a=a**b -> a**=b  

note : Here Insted Of b we can Take Any Number Also 

'''


a=20
b=30
a+=b
print(a)


#4. Logical Operator : NOTE it also exicute whean case is true or give in print ture or falsr case 

a=20
b=30

# #and 
print(a==b and a>=b)
# #or
print(a==b or a>=b)
# #not
print(not(a==b and a>=b))


#Type Conversion : 

'''
1.Conversion : Done By Systuem 
2.Type Casting : Done By User 
'''

#Conversion : 

a= 20
b= 2.34
print(a+b)


#NOTE : IN String + Int / Float Not Posible : But Only Type Cast Work Whean Literal Works : 

a = "2" #String 
b= 3
print(a+b)


a = int("2") #String  -> int Type Cast
b= 3
print(a+b)


#Input In Python : 

# synatax : input()

# input("Enter Age : ")

# NOTE : By Default Whatever We Are Taking It Is In String 

#Example : 
var = input("Enter Age : ")
print (type(var))


#-> After Type cast : 

var = int(input("Enter Age : "))
print (type(var))
print(var)


for i in range(3):
    pass
print(i)