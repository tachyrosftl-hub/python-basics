"""
Day 2.5 - Algorithm Practice Menu + Auto Tests
Author: Deus
Description:
    Interactive CLI to test Day 2.5 problems:
    1. Best Time to Buy and Sell Stock
    2. Contains Duplicate
    3. Valid Parentheses
    Includes automated test cases for quick verification.
"""

# ------------------ Algorithm Implementations ------------------ #

def best_time_to_buy_sell(prices):
    """Calculates the max profit from stock prices."""
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


def contains_duplicate(nums):
    """Checks if a list contains duplicates."""
    return len(nums) != len(set(nums))


def valid_parentheses(s):
    """Checks if a string has valid parentheses."""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False
    return not stack

# ------------------ Test Cases ------------------ #

def run_tests():
    print("\nRunning automated tests...\n")

    # Best Time to Buy/Sell Stock
    assert best_time_to_buy_sell([7, 1, 5, 3, 6, 4]) == 5
    assert best_time_to_buy_sell([7, 6, 4, 3, 1]) == 0
    print("✅ best_time_to_buy_sell passed")

    # Contains Duplicate
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    print("✅ contains_duplicate passed")

    # Valid Parentheses
    assert valid_parentheses("()") is True
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("(]") is False
    assert valid_parentheses("([)]") is False
    assert valid_parentheses("{[]}") is True
    print("✅ valid_parentheses passed")

    print("\nAll tests passed!\n")

# ------------------ Interactive Menu ------------------ #

def menu():
    while True:
        print("\nDay 2.5 Algorithm Menu")
        print("1. Best Time to Buy/Sell Stock")
        print("2. Contains Duplicate")
        print("3. Valid Parentheses")
        print("4. Run Automated Tests")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                prices = list(map(int, input("Enter stock prices separated by space: ").split()))
                print("Max Profit:", best_time_to_buy_sell(prices))
            except ValueError:
                print("Invalid input. Please enter integers only.")

        elif choice == '2':
            try:
                nums = list(map(int, input("Enter numbers separated by space: ").split()))
                print("Contains Duplicate:", contains_duplicate(nums))
            except ValueError:
                print("Invalid input. Please enter integers only.")

        elif choice == '3':
            s = input("Enter parentheses string: ")
            print("Valid Parentheses:", valid_parentheses(s))

        elif choice == '4':
            run_tests()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

# ------------------ Entry Point ------------------ #

if __name__ == "__main__":
    menu()
