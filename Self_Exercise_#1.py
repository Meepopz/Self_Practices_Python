#Exercise 1 - Simple Grading System

name = input("What is your name?: ")
year_level = input("Program and Year Level: ")

print("\n")

user = input("From 0-100, enter the score you've got: ")

score = int(user)

if score >= 90 and score <= 100:
    print("Graded A: Excellent work!")

elif score >= 80 and score <= 89:
    print("Graded B: Excellent work!")

elif score >= 70 and score <= 79:
    print("Graded C: Fair Job!")

elif score >= 60 and score <= 69:
    print("Grade D: Barely")

else:
    print("Graded F")
