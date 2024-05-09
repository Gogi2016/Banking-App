import random
import string
import password_generator

# Function to generate a random password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

# Function to handle deposits
def deposit(balance):
    try:
        amount = float(input("How much would you like to deposit? "))
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        balance += amount
        print(f"Deposit of ${amount} successful.")
    except ValueError as e:
        print("Invalid input. Please enter a valid amount.")
    return balance

# Function to handle withdrawals
def withdraw(balance):
    try:
        amount = float(input("How much would you like to withdraw? "))
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > balance:
            raise ValueError("Insufficient funds")
        balance -= amount
        print(f"Withdrawal of ${amount} successful.")
    except ValueError as e:
        print("Invalid input. Please enter a valid amount.")
    return balance

# Function to update transaction log
def update_transaction_log(transaction_type, amount):
    with open("TransactionLog.txt", "a") as log_file:
        log_file.write(f"{transaction_type}: ${amount}\n")

# Function to update bank data
def update_bank_data(balance):
    with open("BankData.txt", "w") as bank_data_file:
        bank_data_file.write(str(balance))

# Function to read current balance from bank data
def read_balance():
    with open("BankData.txt", "r") as bank_data_file:
        balance = float(bank_data_file.read())
    return balance

def main():
    # Initialize balance
    balance = read_balance()
    
    # Interaction loop
    while True:
        print(f"Current balance: ${balance}")
        transaction = input("Would you like to make a transaction? (Yes/No) ").lower()
        if transaction != "yes":
            break
        
        transaction_type = input("Would you like to make a deposit or withdrawal? (Deposit/Withdrawal) ").lower()
        if transaction_type == "deposit":
            balance = deposit(balance)
            update_transaction_log("Deposit", balance)
        elif transaction_type == "withdrawal":
            balance = withdraw(balance)
            update_transaction_log("Withdrawal", balance)
        else:
            print("You provided an invalid input.")
        
        update_bank_data(balance)
    
    print(f"Final balance: ${balance}")

if __name__ == "__main__":
    main()
