#Chapter 4 : Dictionary & Set : 


# 1. Store the following word meanings in a Python dictionary:
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

word_meaning = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}
print(word_meaning)


# 2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students?
# Subjects list:
# "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

set1 = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(set1)
print(len(set1))


# 3. Write a program (WAP) to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary
# Add entries one by one
# Use subject name as key and marks as value

student = {}
new_data = {
    "subject" : {
        "Hindi" : 90,
        "English" : 99,
        "Maths" : 98
    }
}
student.update(new_data)
print(student)


# 4. Figure out a way to store 9 & 9.0 as separate values in a set.
# (You can take help of built-in data types)

sep = {9 , '9.0'}
print(sep)