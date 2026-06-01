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