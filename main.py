'''
Create a Python class called BankAccount that simulates a simple bank account. The class should have the following functionalities:
It should have a constructor that accepts the account_holder name and initial balance (initial_balance), setting the balance to zero if the initial balance is not provided.
'''
class BankAccount:

    def __init__(self, account_holder : str, initial_balance :float = 0.0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    #A method called deposit that accepts an amount and adds it to the account balance, and then returns the updated balance.
    def deposit(self, amount):
        self.initial_balance = self.initial_balance + amount
        return (f"\nYour Account balance: {self.initial_balance}\n")

    #A method called withdraw that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. 
    #If there are insufficient funds, it should print an error message and leave the balance unchanged.
    def withdraw(self, amount):
        if self.initial_balance >= amount:
            self.initial_balance = self.initial_balance - amount
            return (f"\nYour Account balance: {self.initial_balance}\n")
        else:
            return (f"\nYour Account balance: {self.initial_balance}. you have insufficient amount, can't withdraw {amount}\n")

    #A method called get_balance that returns the current account balance.
    def get_balance(self):
        return (f"\nYour Account balance: {self.initial_balance}\n")

    #A method called get_account_holder that returns the name of the account holder.
    def get_account_holder(self):
        return (f"\nThe Account holder name: {self.account_holder}\n")

account1 = BankAccount("Safa")

print(account1.deposit(10))
print(account1.withdraw(20))
print(account1.get_balance())
print(account1.get_account_holder())

