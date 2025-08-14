class BankAccount:
    _account_counter = 1000  

    def __init__(self, balance):
        BankAccount._account_counter += 1
        self.account_number = BankAccount._account_counter
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        return f"Account No: {self.account_number}, Balance: {self.__balance}"


# ---------------------------
# Savings Account subclass
# ---------------------------
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)


# Current Account subclass

class CurrentAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            # Directly modify balance using base class method
            current_balance = self.get_balance()
            if amount > current_balance:
                overdraft_used = amount - current_balance
                print(f"Overdraft used: {overdraft_used}")
            self._BankAccount__balance = current_balance - amount  
        else:
            print("Amount exceeds balance + overdraft limit.")


# ---------------------------
# Example Usage
# ---------------------------
# Savings account
s_acc = SavingsAccount(1000, 5)
s_acc.deposit(500)
s_acc.add_interest()
print(s_acc.get_account_info())  # Interest will be added

# Current account
c_acc = CurrentAccount(2000, 1000)
c_acc.withdraw(2500)  # uses overdraft
print(c_acc.get_account_info())

