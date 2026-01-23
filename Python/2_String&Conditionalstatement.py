# Chapter :  2 (String And Conditional Statements)


# String : It Is An Data Type In Python , Where Collection of Character Value In Sequence . 

# Example 1 : Creation Of String : 

str1 = "I am 20 Years Old" # For Storting Multiple Characters 
str2 = 'Age'  # For Storing Single Word 
str3 = '''I am SWE At Microsoft" # Use This For Multiple Words there ''' # This Is Also Used To Declare Multiple Word Of a Character By Avoiding The Case Of They are playing"s or They are playing's .

print(str1)
print(str2)
print(str3)


# Example 2 : Escape Sequence Used To Shift To Another Line Of String Without Giveing Space . 

str1 = "This Is So Sweet,\nI like this Food." # This For Next Line 
print(str1)


str1 = "This Is So Sweet,\tI like this Food." # This for Tab Space 
print(str1)


# String Operator :

'''
1.Concatination
2.Length 
''' 

# 1. Concatination : NOTE Used For Adding Two String Value 

# Example 1 :  

str1 = "Man"
str2 = "Women"
print(str1+str2)


# or 

str1 = "Man"
str2 = "Women"
final_str = str1+str2
print(final_str)


# Example 2 : 

str1 = "Man"
str2 = "Women"
final_str = str1+" "+str2 # This We Use For Adding Space Between Two String . 
print(final_str)


# 2. len : NOTE Used To Find Lenghth Of The String 

str1 = "Man"
str2 = "Women"
final_str = str1+" "+str2 # This We Use For Adding Space Between Two String . 
print(len(final_str))


#OR 

str1 = "Man"
str2 = "Women"
final_str = len(str1+" "+str2) # This We Use For Adding Space Between Two String . 
print(final_str)


# String Indexing :

# 1.Postive Index : In Each An Every Character Of Their Is Some Index Value location From 0 which is from start -> last element : 
# NOTE :This Is Only Helpful For Printing We Can't Update The String  

str = "My Name Is Aditya Kumar"
print(str[1]) 


# or 

# NOTE : If Web Will Try Update Using String Indexing It Through Error .

str = "My Name Is Aditya Kumar"
# str[2] = "a"
print(str[2])


# 2. Negative Index : In Each An Every Character Of Their Is Some Index Value location From -1 which is from end -> start element and incresing -ve :
# NOTE : Only Applicable For Slicing This Concept : 

# String Sliceing : If We Wants To Print An Sring from Some Indexes To Some Indexes So We Use Slicing .

str = "My Fav Programming Language Is JavaScript"
print(str[8:15])  # str[x:y] From x to y-1 it will take .


#Cases In String Slicing : 
#-> NOTE : A. From First To X Place , B. From X to Last Place : 

# Case A : From First To X Place : 
str = "Probability Is My Fav Subject"
print(str[:5]) # Here We Won't Mentioned Any Index Value For Start So It Consider From 0 .

# Case B : From X Place to Last: 
str = "Probability Is My Fav Subject"
print(str[5:len(str)]) # Here Insted Of Last We Mentioned len(str) which take the last as length; len(str)

# Or

str = "Probability Is My Fav Subject"
print(str[10:]) # Here We Won't Mentioned Any Index Value For last So It Consider From as last .


#NOTE : Use Negative Index In Slicing : 
str = "Probability Is My Fav Subject"
print(str[-5:-1]) #From Last Element As -1 to any as -x .


#Function In String :
 
'''
1. endswith()  # Gives In True Or False
2. Capitalize()
3. find()
4. replace(old,new)
5. count()

'''
# Example :

str = "Ram Baran Verma Is My Maths Professor For Sem 4"
print(str.endswith("Sem 4"))


str = "ram Baran Verma Is My Maths Professor For Sem 4"
print(str.capitalize()) # It Capitalize The First Index Value 

str = "Ram Baran Verma Is My Maths Professor For Sem 4"
print(str.find("a"))   #It Will give at what Index place that string Character Exist 

str = "Ram Baran Verma Is My Maths Professor For Sem 4"
print(str.replace('a','b'))  #It Will Change The String Character Place with New Element .

str = "Ram Baran Verma Is My Maths Professor For Sem 4"
print(str.count("a"))  #Count Specipic String Character That How Many Num Of Times It Is Repating 


# Conditional Satements In Python : A) In an Python We Use if-elif-else we use as Conditional Satement For Checking Wheather The Given Is Correct Or Wrong If It is Then Based Upon Cases It Will Work  .

'''
1. If Ladder 
2. If - elif case
3. If-else case  
4. If-elif-else Case
'''

# Example : 1. If Ladder

a = 12
if(a>5):
print("Hi")  # NOTE Here After if  case in next line first we take 4 spaces as tab space
if(a>3): 
# NOTE Here As We Saw Both The Cases Is Exicuted Because in if if case It Will check both even any one is true or both is true 
print("Aditya")  


#Example : If-elif Case : 

a=12
if(a>5):                  # NOTE First Exicute -> True Thean Terminate this ; Even It Is Having First a>3 
print("Hi")
elif(a>3):           
print("Aditya")


#Example : If - else Case  : 

age = 12
if(age>18):
print("Elligible For Vote")
else:
print("Not Elligible For Vote")


# Example : If - elif - else case : 
#Based Upon Input Of Day Num By User Print Day ;

day = int(input("Enter Day Num : "))
if(day == 1):
print("Monday")
elif(day == 2):
print("Tuesday")
elif(day == 3):
print("Wednesday")
elif(day == 4):               # NOTE : Here While Exicuting An Program It Exicute To Next When Any One CaseIs Incorrect
print("Thrusday")
elif(day == 5):
print("Friday")
elif(day == 6):
print("Saturday")
elif(day == 7):
print("Sunday")
else: 
print("Wrong Input!")


# B) Nested Loop Using If-elif-else : 
'''
Syntax: 

# NOTE :Here We Use Multiple Cases : 

if(condition):
    if(condition):  
    print("Case")
    else:
    print("Case2")
else:
    print("Case Is False")
'''


