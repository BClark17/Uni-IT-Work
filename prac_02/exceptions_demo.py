"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the entered value is not
        an appropriate number (e.g.when a letter is typed instead)
2. When will a ZeroDivisionError occur? (When the user enters
        zero as the denominator)
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
        You could write an if statement to test if the denominator is
        greater than zero, if it is't, the user is required to re-enter
        the denominator value.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        denominator = int(input("Denomiator cannot be equal to 0. Please Re-enter: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")