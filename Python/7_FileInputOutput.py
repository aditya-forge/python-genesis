# Lecture : 7 (File Input / Output)

import os

#1. Writing to a File 
with open("sample.txt", "w") as f:
    f.write("Hello, File I/O!\n")
    f.write("Python makes reading and writing files simple.\n")
    f.write("This is line 3.\n")

print("File written successfully.")


#2. Reading the Entire File
with open("sample.txt", "r") as f:
    content = f.read()
    print("\n--- Full File Content ---")
    print(content)


#3. Reading Line by Line 
with open("sample.txt", "r") as f:
    print("--- Line by Line ---")
    for line in f:
        print(line, end="")   # line already has \n


#4. readlines() 
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("\n--- readlines() output ---")
    print(lines)
    print(f"Total lines: {len(lines)}")


#5. Appending to a File 
with open("sample.txt", "a") as f:
    f.write("Appended line 4.\n")

print("\nLine appended.")


#6. Working with File Paths
print(f"\nFile exists: {os.path.exists('sample.txt')}")
print(f"File size  : {os.path.getsize('sample.txt')} bytes")
print(f"Current dir: {os.getcwd()}")


#7. Writing & Reading with 'r+' (read-write) 
with open("notes.txt", "w") as f:
    f.write("Line A\nLine B\nLine C\n")

with open("notes.txt", "r+") as f:
    data = f.read()
    f.write("Line D\n")   # appends at EOF since we read to end
    print("\n--- notes.txt ---")
    print(data)


#8. Exception Handling with Files 
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(f"\nError: {e}")


#9. Cleanup ─
for fname in ("sample.txt", "notes.txt"):
    if os.path.exists(fname):
        os.remove(fname)
        print(f"Removed {fname}")
