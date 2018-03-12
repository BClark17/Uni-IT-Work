"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter your score:"))
if 0 <= float(score) < 50:
    print("Bad Score")
elif 50 <= float(score) < 90:
    print("Passable Score")
elif 90 <= float(score) < 100:
    print("Excellent")
else:
    print("Please input a score value from 0 to 100.")