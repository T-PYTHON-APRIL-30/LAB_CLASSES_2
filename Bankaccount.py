# Create a Python class called BankAccount that simulates a simple bank account:
class BankAccount:
    def __init__(self,holderName: str,initial_balance:int) -> None: # It should have a constructor that accepts the account_holder name and initial balance (initial_balance).
        self.holderName = holderName
        self.initial_balance = initial_balance

    def deposit(self, amount:int): #A method called deposit that accepts an amount.
         # and adds it to the account balance, and then returns the updated balance.
        self.initial_balance += amount
        return self.initial_balance
    
    def withdraw(self, amount:int): #A method called withdraw that accepts an amount.
        if self.initial_balance < amount:
           raise f"The balance in your account is {self.initial_balance}, which is less than to complete your request"
        else:
            self.initial_balance -= amount #and subtracts it from the account balance.
        return f"The balance after updating is {self.initial_balance}" # returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
    def get_balance(self): #A method called get_balance that returns the current account balance.
        return self.initial_balance
    
    def get_account_holder(self): #A method called get_account_holder that returns the name of the account holder.
        return f"her name : {self.holderName}"
    



account1 = BankAccount("Juhaina", 30000)
print(account1.deposit(250))
print(account1.withdraw(10000))
print(account1.get_balance())
print(account1.get_account_holder())