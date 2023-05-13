# simulates a simple bank account

class BankAccount:
    # constructor: method that is called when an object is created of a class
    def __init__(self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    # accepts an amount and adds it to the account balance
    def deposit(self, amount):
        self.initial_balance += amount
        return self.initial_balance
    
    # accepts an amount and subtracts it from the account balance
    def withdraw(self, amount):
        if amount > self.initial_balance:
            print("insufficient funds")
            # return self.initial_balance ?
        else:
            self.initial_balance -= amount
            return self.initial_balance
    
    # returns current account balance.
    def get_balance(self):
        return self.initial_balance

    # returns the name of the account holder
    def get_account_holder(self):
        return self.account_holder
    
account = BankAccount(input("enter your name:"))

print()
print("account holder:", account.get_account_holder())
print("current balance:", account.get_balance())

print()
amount_deposited = float(input("enter amount to be deposited:"))
print("current balance:", account.deposit(amount_deposited))

print()
amount_withdrew = float(input("enter amount to be withdrawn:"))
print("current balance:", account.withdraw(amount_withdrew))