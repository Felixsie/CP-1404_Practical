"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))
while score < 0:
    print("Invalid score")

if score > 100:
    print("Invalid score")
elif  score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")