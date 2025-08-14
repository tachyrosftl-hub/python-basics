"""
Day 1 Refactored - Python Basics
Author: Deus
Description:
    Refactored version of Day 1 code with functions, docstrings,
    and basic input validation for cleaner and reusable code.
"""


def hello_world():
    """Prints Hello World."""
    print("Hello, World!")


def get_user_info():
    """Prompts user for name and age, then prints the result."""
    name = input("Enter your name: ")

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid age. Please enter a number.")

    print(f"Your name is {name} and you are {age} years old.")


def calculate_numbers(num):
    """Calculates and prints square, cube, and factorial of a number."""
    square = num ** 2
    cube = num ** 3

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print(f"Square: {square}, Cube: {cube}, Factorial: {factorial}")


def reverse_string(text):
    """Reverses a string without using slicing."""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    print("Reversed string:", reversed_text)


def reverse_string_indexing(text):
    """Reverses a string using indexing."""
    reversed_text = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]
    print("Reversed string (indexing method):", reversed_text)


def list_operations(numbers):
    """Calculates and prints sum, max, and min of a list without built-ins."""
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


if __name__ == "__main__":
    hello_world()

    get_user_info()

    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid number. Please enter an integer.")

    calculate_numbers(num)

    text = input("Enter a string: ")
    reverse_string(text)
    reverse_string_indexing(text)

    numbers = [3, 1, 4, 1, 5, 9]
    list_operations(numbers)
