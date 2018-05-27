"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    result= get_result(score)

    print("Your grade is: {}".format(result))



def get_result(point):

    if point < 0 or point > 100:
        grade= "Invalid score! Please put your score correctly.."

    elif point >= 90:
        grade= "Excellent"

    elif point >= 50:
        grade= "Passable"

    else:
        grade= "Bad"

    return grade



main()