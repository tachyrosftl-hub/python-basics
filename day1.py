# 1. Hello World
print("Hello, World!")

# 2. Input & Output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Your name is {name} and you are {age} years old.")

# 3. Square, cube, factorial
num = int(input("Enter a number: "))
square = num ** 2
cube = num ** 3

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"Square: {square}, Cube: {cube}, Factorial: {factorial}")

# 4. Reverse a string manually
text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed string:", reversed_text)

# 5. List operations without built-ins
numbers = [3, 1, 4, 1, 5, 9]
total = 0
max_num = numbers[0]
min_num = numbers[0]

for n in numbers:
    total += n
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print(f"Sum: {total}, Max: {max_num}, Min: {min_num}")
