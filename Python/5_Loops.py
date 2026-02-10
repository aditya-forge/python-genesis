# Leacture : 5 (Loops -> For , While Loop)

#Table Of Content :

'''

 1. While loop : 
 2. Break & Continew Statement's
 3. For Loop  -> Case Of Sequential Search 
 4. range() function
 5. pass statement

 '''

#1. While Loop : NOTE : It Will Keep Executing Until Condition Becomes False

i = 1
while i <= 5:
    print("Count:", i)
    i += 1


#2. While Loop With Accumulator : NOTE : Sum All Numbers From 1 to N

n = 10
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum of 1 to", n, "=", total)


#3. Infinite Loop With Break : NOTE : break Stops Loop Immediately

while True:
    val = input("Enter 'quit' to stop: ")
    if val == "quit":
        print("Loop exited!")
        break
    print("You typed:", val)


#4. Continue Statement : NOTE : Skips Current Iteration And Goes To Next

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


#5. For Loop With List : NOTE : Iterates Over Each Element Directly

fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print("I like", fruit)


#6. For Loop With String : NOTE : Each Character Is An Element

name = "Aditya"
for ch in name:
    print(ch, end="-")
print()


#7. range() Function : NOTE : Generates Sequence Of Numbers

# range(stop) - 0 to stop-1
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop) - start to stop-1
for i in range(3, 8):
    print(i, end=" ")
print()

# range(start, stop, step) - with custom step
for i in range(0, 20, 3):
    print(i, end=" ")
print()


#8. Nested Loops : NOTE : Inner Loop Runs Completely For Each Outer Iteration

# Print a pattern
for row in range(1, 6):
    for col in range(1, row + 1):
        print("*", end=" ")
    print()


#9. Multiplication Table Using For Loop

num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#10. Counting In A List Using While

numbers = [10, 25, 30, 10, 50, 10, 40]
target = 10
count = 0
idx = 0
while idx < len(numbers):
    if numbers[idx] == target:
        count += 1
    idx += 1
print(f"{target} appears {count} times")


#11. Sequential Search Using For Loop : NOTE : Find Element In List

data = [15, 22, 8, 33, 41, 19]
key = 33
found = False
for i in range(len(data)):
    if data[i] == key:
        print(f"Found {key} at index {i}")
        found = True
        break
if not found:
    print(f"{key} not found in list")


#12. Pass Statement : NOTE : Placeholder When Body Is Not Ready Yet

for i in range(5):
    if i == 3:
        pass  # will handle later
    else:
        print(i)


#13. While With Else : NOTE : else Block Runs When Condition Becomes False Normally

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("While loop finished naturally")


#14. For With Else : NOTE : else Runs Only If Loop Was NOT Broken

for num in [2, 4, 6, 8]:
    if num % 2 != 0:
        print("Found odd number!")
        break
else:
    print("All numbers are even")


#15. Reverse Counting Using range

for i in range(10, 0, -1):
    print(i, end=" ")
print("Go!")