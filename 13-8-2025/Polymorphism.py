class BankAccount:
   
    _account_counter = 1000  

    def __init__(self, balance):
        BankAccount._account_counter += 1
        self.account_number = BankAccount._account_counter 
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        return f"Account No: {self.account_number}, Balance: {self.__balance}"

acc1 = BankAccount(1000)
acc2 = BankAccount(2000)

acc1.deposit(100)


print(acc1.get_account_info())  
print(acc2.get_account_info())  