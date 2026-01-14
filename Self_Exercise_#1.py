#Exercise 1 - Simple Grading System

name = input("What is your name?: ")
year_level = input("Program and Year Level: ")

print("\n")

user = input("From 0-100, enter the score you've got: ")

score = int(user)

if score >= 90 and score <= 100: #we used
    print(f"grade = A")
    print(f"Excellent work")
elif score >= 80 and score <= 89:
    print(f"grade = B")
    print(f"Satisfactory work")
elif score >= 70 and score <= 79:
    print(f"grade = C")
    print(f"Fair job")
elif score > 60 and score <= 69:
    print(f"grade = D")
    print(f"Barely failed, but good enough")
else:
    print(f"grade = F")
    print(f"PAGTUON LAGEH DILI MAG SALIG UG AI")