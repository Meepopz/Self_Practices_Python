#ATM Simulator

print("\n")

print("Show Options: ")
print("1.   --- Deposit---")
print("2.   ---Withdraw---")
print("3. ---Check Balance---")
print("4.     ---Exit---")
print("\n")

options = input("Enter a choice: ")
options = int(options)

Balance = 1000.0

if options == 1:
    deposit = input("Amount of Deposit: ")
    deposit = float(deposit)
    result = Balance + deposit
    print(result)
    print("\n")

if options == 2:
    withdraw = input("Amount of Withdraw: ")
    withdraw = float(withdraw)
    if withdraw <= Balance:
        result = Balance - withdraw
        print(result)
    else:
        print("Insufficient funds!")
        print("\n")

    Balance = 1000.0

elif options == 3:
    print(f"Current balance: {Balance}")

elif options == 4:
    print("Thank you for using the ATM.")

else:
    print("Incorrect input!")
    print("\n")