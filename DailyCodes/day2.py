"""
Day 2 - Lists, Strings, and Conditionals
Author: Deus
Description:
    Core Python exercises focusing on control flow, 
    string/list manipulation, and algorithm thinking.
"""


def is_prime(n):
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_vowels(s):
    """Count the number of vowels in the string s."""
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list without using sort().
    Uses two-pointer technique.
    """
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def are_anagrams(s1, s2):
    """
    Return True if s1 and s2 are anagrams, ignoring spaces and case.
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)


def menu():
    """Runs an interactive menu for testing the functions."""
    while True:
        print("\n=== Day 2 Function Tester ===")
        print("1. Prime Checker")
        print("2. Vowel Counter")
        print("3. Merge Sorted Lists")
        print("4. Anagram Checker")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                num = int(input("Enter a number: "))
                print(f"{num} is prime? {is_prime(num)}")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == "2":
            s = input("Enter a string: ")
            print(f"Vowel count: {count_vowels(s)}")

        elif choice == "3":
            try:
                list1 = list(map(int, input("Enter first sorted list (space-separated): ").split()))
                list2 = list(map(int, input("Enter second sorted list (space-separated): ").split()))
                print("Merged list:", merge_sorted_lists(list1, list2))
            except ValueError:
                print("Invalid input. Please enter only integers.")

        elif choice == "4":
            s1 = input("Enter first string: ")
            s2 = input("Enter second string: ")
            print("Are anagrams?", are_anagrams(s1, s2))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
