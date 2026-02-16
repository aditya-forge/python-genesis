# Lecture : 6 (Functions & Recursion)

#1. Defining and Calling Functions
def greet(name):
    """Return a personalised greeting."""
    return f"Hello, {name}!"

print(greet("Aditya"))


#2. Default & Keyword Arguments 
def power(base, exp=2):
    return base ** exp

print(power(3))        # 9  (uses default exp=2)
print(power(2, 10))    # 1024


#3. *args and **kwargs
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4, 5))   # 15


def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_info(name="Aditya", course="B.Tech CSE", year=2)


#4. Lambda Functions
square = lambda x: x * x
print(square(7))   # 49

# Sort a list of tuples by second element using lambda
pairs = [(1, "b"), (3, "a"), (2, "c")]
pairs.sort(key=lambda p: p[1])
print(pairs)   # [(3, 'a'), (1, 'b'), (2, 'c')]


# ── 5. Recursion

# Factorial
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
print(factorial(0))   # 1


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])  # [0,1,1,2,3,5,8,13,21,34]


# Sum of digits using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))   # 10


# Tower of Hanoi
def hanoi(n, src="A", dest="C", aux="B"):
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return
    hanoi(n - 1, src, aux, dest)
    print(f"Move disk {n} from {src} to {dest}")
    hanoi(n - 1, aux, dest, src)

hanoi(3)
