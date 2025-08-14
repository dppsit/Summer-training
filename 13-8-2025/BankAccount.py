import random

# =========================
# Base Class
# =========================
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = self.generate_account_number()
        self.account_holder = account_holder
        self.balance = balance

    @staticmethod
    def generate_account_number():
        # Generate 16-digit account number
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance}")

# =========================
# Child Class - Saving Account
# =========================
class SavingAccount(BankAccount):
    INTEREST_RATE = 4  # Bank decided interest rate in %

    def apply_interest(self):
        interest = self.balance * (SavingAccount.INTEREST_RATE / 100)
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied at {SavingAccount.INTEREST_RATE}% rate.")

# =========================
# Child Class - Current Account
# =========================
class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 50000  # Bank decided overdraft limit

    def withdraw(self, amount):
        if self.balance - amount >= -CurrentAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully (Overdraft facility used if needed).")
        else:
            print("Withdrawal exceeds overdraft limit.")

# =========================
# Program Execution
# =========================
def main():
    account_type = input("Enter account type (saving/current): ").strip().lower()
    name = input("Enter account holder name: ").strip()
    balance = float(input("Enter initial balance: "))

    if account_type == "saving":
        account = SavingAccount(name, balance)
        print("\nYour Saving Account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Interest Rate (Bank Fixed): {SavingAccount.INTEREST_RATE}%")
    elif account_type == "current":
        account = CurrentAccount(name, balance)
        print("\nYour Current Account has been created successfully.")
        print(f"Account Number: {account.account_number}")
        print(f"Overdraft Limit (Bank Fixed): ₹{CurrentAccount.OVERDRAFT_LIMIT}")
    else:
        print("Invalid account type! Please restart the program.")
        return

    while True:
        print("\nChoose operation:")
        if isinstance(account, SavingAccount):
            print("1. Deposit\n2. Withdraw\n3. Display Balance\n4. Apply Interest\n5. Exit")
        else:
            print("1. Deposit\n2. Withdraw\n3. Display Balance\n5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.display_balance()
        elif choice == "4" and isinstance(account, SavingAccount):
            account.apply_interest()
        elif choice == "5":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
