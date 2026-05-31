# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Project 01 : ATM SIMULATION PROJECT


import os

balance = 10000
pin = "1234"

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    entered_pin = input("Enter PIN: ")

    if entered_pin != pin:
        print("Wrong PIN!")
        continue

    choice = input("Enter Choice: ")

    if choice == "1":
        print("Current Balance =", balance)

    elif choice == "2":
        amount = float(input("Enter Deposit Amount: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == "3":
        amount = float(input("Enter Withdraw Amount: "))

        if amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Please Collect Cash")

    elif choice == "4":
        print("Thank You For Using ATM")
        break

    else:
        print("Invalid Choice")





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   projetc 02 : BMI CALCULATOR PROJECT



try:

    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (meter): "))

    bmi = weight / (height ** 2)

    print("BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")

    elif bmi < 25:
        print("Normal Weight")

    elif bmi < 30:
        print("Overweight")

    else:
        print("Obese")

except ValueError:
    print("Please Enter Valid Numbers")
