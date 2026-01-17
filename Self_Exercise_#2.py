#Exercise 2 -

user_age = input("How old are you currently?: ")

user_age = int(user_age)

if user_age <= 12:
    print("Children under 12 pay 100 pesos")

elif  user_age >= 13 and user_age <= 17:
    print("Teenagers between 13 to 17 pay 150 pesos")

elif user_age >= 18 and user_age <= 59:
    print("Adults between 18 and 59  pay 200 pesos")

elif user_age >= 60:
    print("Senior Citizens pay 120 pesos")

else:
    print("HOLD YOUR HOE")