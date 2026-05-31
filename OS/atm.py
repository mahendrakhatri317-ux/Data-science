import pandas as pd
import os

# CSV file name
FILE_NAME = "accounts.csv"

# Check file exists
if not os.path.exists(FILE_NAME):
    print("Account file not found!")
    exit()

# Read CSV file
data = pd.read_csv(FILE_NAME)

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Login
account_no = int(input("Enter Account Number: "))
pin = int(input("Enter PIN: "))

# Find user
user = data[(data['Account'] == account_no) & (data['PIN'] == pin)]

if user.empty:
    print("Invalid Account Number or PIN")
    exit()

index = user.index[0]

print("\nLogin Successful!")

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Check Balance
    if choice == '1':
        balance = data.loc[index, 'Balance']
        print(f"Your Balance: ₹{balance}")

    # Deposit
    elif choice == '2':
        amount = int(input("Enter amount to deposit: ₹"))

        data.loc[index, 'Balance'] += amount

        print("Money Deposited Successfully!")

    # Withdraw
    elif choice == '3':
        amount = int(input("Enter amount to withdraw: ₹"))

        if amount > data.loc[index, 'Balance']:
            print("Insufficient Balance!")
        else:
            data.loc[index, 'Balance'] -= amount
            print("Please collect your cash!")

    # Change PIN
    elif choice == '4':
        new_pin = int(input("Enter New PIN: "))
        data.loc[index, 'PIN'] = new_pin

        print("PIN Changed Successfully!")

    # Exit
    elif choice == '5':

        # Save updated data
        data.to_csv(FILE_NAME, index=False)

        print("Thank You for Using ATM!")
        break

    else:
        print("Invalid Choice!")