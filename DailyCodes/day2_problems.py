"""
Day 2 - Algorithm Practice (Interactive Mode)
Author: Deus
Description:
    Solutions for 3 LeetCode problems with:
    - Input validation
    - Interactive testing menu
"""

# ------------------ PROBLEM SOLUTIONS ------------------

def two_sum(nums, target):
    """Return indices of the two numbers that add up to target."""
    num_map = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


def is_palindrome(s):
    """Check if a string is a palindrome (ignores non-alphanumeric)."""
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]


def fizz_buzz(n):
    """Return a list from 1 to n with FizzBuzz rules."""
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# ------------------ INPUT VALIDATION HELPERS ------------------

def get_int(prompt, min_value=None, allow_zero=True):
    """Get an integer from the user with optional min value check."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Try again.")
                continue
            if not allow_zero and value == 0:
                print("Zero is not allowed. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_int_list(prompt):
    """Get a list of integers from user input."""
    while True:
        raw = input(prompt).strip()
        try:
            nums = [int(x) for x in raw.split()]
            if not nums:
                print("List cannot be empty.")
                continue
            return nums
        except ValueError:
            print("Invalid list. Enter space-separated integers only.")

# ------------------ INTERACTIVE MENU ------------------

def main():
    while True:
        print("\n=== Day 2 Interactive Menu ===")
        print("1. Two Sum")
        print("2. Valid Palindrome")
        print("3. FizzBuzz")
        print("4. Exit")

        choice = get_int("Choose an option (1-4): ", 1, allow_zero=False)

        if choice == 1:
            nums = get_int_list("Enter numbers (space-separated): ")
            target = get_int("Enter target sum: ")
            print("Indices:", two_sum(nums, target))

        elif choice == 2:
            text = input("Enter a string: ")
            print("Is palindrome?", is_palindrome(text))

        elif choice == 3:
            n = get_int("Enter n (max number): ", min_value=1, allow_zero=False)
            print("FizzBuzz Output:", fizz_buzz(n))

        elif choice == 4:
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
