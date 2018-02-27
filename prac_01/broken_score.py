"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter your score:"))
if float(score) < 50 and float(score) >= 0:
    print("Bad Score")
elif float(score) < 90 and float(score) >= 50:
    print("Passable Score")
elif float(score) < 100 and float(score) >= 90:
    print("Excellent")
else:
    print("Please input a score value from 0 to 100.")