class BankAccount:
    def __init__(self,account_holder: str,initial_balance:int): 
        self.account_holder = account_holder
        self.initial_balance = initial_balance
        initial_balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    def deposit(self, amount:int):
        self.initial_balance += amount
        return self.initial_balance

    def withdraw(self, amount:int): 
        if self.initial_balance < amount:
           print("\n Insufficient balance ")
        else:
            self.initial_balance -= amount
        return f"The balance after updating is {self.initial_balance}" 
    def get_balance(self): 
        return self.initial_balance
    def get_account_holder(self):
        return f"account_holder name is : {self.account_holder}"
    
account = BankAccount("fasial", 200)
print("your amounts is 200")
print("your amount after deposit",account.deposit(10))
print("you withdraw this amount,",account.withdraw(20))
print(account.get_balance())
print(account.get_account_holder())