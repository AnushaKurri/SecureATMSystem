import hashlib
import json
import os
import getpass

class SecureATM:
    def __init__(self, data_file="users.json"):
        self.data_file = data_file
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return json.load(file)
        return {}

    def save_users(self):
        with open(self.data_file, "w") as file:
            json.dump(self.users, file, indent=4)

    def hash_pin(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()

    def register_user(self, account_number, pin, balance=0):
        if account_number in self.users:
            print("Account already exists!")
            return False
        hashed_pin = self.hash_pin(pin)
        self.users[account_number] = {"pin": hashed_pin, "balance": balance}
        self.save_users()
        print("Account created successfully!")
        return True

    def authenticate_user(self, account_number, pin):
        if account_number in self.users:
            hashed_pin = self.hash_pin(pin)
            if self.users[account_number]["pin"] == hashed_pin:
                return True
        return False

    def get_balance(self, account_number):
        return self.users[account_number]["balance"]

    def deposit(self, account_number, amount):
        if amount > 0:
            self.users[account_number]["balance"] += amount
            self.save_users()
            print(f"Deposited ${amount}. New Balance: ${self.get_balance(account_number)}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, account_number, amount):
        if 0 < amount <= self.users[account_number]["balance"]:
            self.users[account_number]["balance"] -= amount
            self.save_users()
            print(f"Withdrawn ${amount}. New Balance: ${self.get_balance(account_number)}")
        else:
            print("Invalid or insufficient funds!")

    def atm_interface(self):
        while True:
            print("\nWelcome to Secure ATM")
            print("1. Register\n2. Login\n3. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                acc_num = input("Enter a new account number: ")
                pin = getpass.getpass("Set a PIN: ")
                self.register_user(acc_num, pin)
            
            elif choice == "2":
                acc_num = input("Enter account number: ")
                pin = getpass.getpass("Enter PIN: ")
                if self.authenticate_user(acc_num, pin):
                    print("Login successful!")
                    while True:
                        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Logout")
                        option = input("Choose an option: ")
                        
                        if option == "1":
                            print(f"Your balance: ${self.get_balance(acc_num)}")
                        elif option == "2":
                            amount = float(input("Enter deposit amount: "))
                            self.deposit(acc_num, amount)
                        elif option == "3":
                            amount = float(input("Enter withdrawal amount: "))
                            self.withdraw(acc_num, amount)
                        elif option == "4":
                            print("Logging out...")
                            break
                        else:
                            print("Invalid option!")
                else:
                    print("Authentication failed! Incorrect account number or PIN.")
            
            elif choice == "3":
                print("Thank you for using Secure ATM!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    atm = SecureATM()
    atm.atm_interface()
