# # LAB_CLASSES_2

# **Exercise:**

# Create a Python class called `BankAccount` that simulates a simple bank account. 
# The class should have the following functionalities:

# 1. It should have a constructor that accepts the `account_holder` name and initial balance 
# (`initial_balance`) =0, setting the balance to zero if the initial balance is not provided.

# 2. A method called `deposit` that accepts an amount and adds it to the account balance, 
# and then returns the updated balance.

# 3. A method called `withdraw` that accepts an amount and subtracts it from the account balance,
# returning the updated balance, but only if there are sufficient funds in the account.
# If there are insufficient funds, it should print an error message and leave the balance unchanged.

# 4. A method called `get_balance` that returns the current account balance.

# 5. A method called `get_account_holder` that returns the name of the account holder.

# ---------

class BankAccount:
    def __init__(self,account_holder:str,initial_balance=0):
        self.account_holder=account_holder
        self.initial_balance=initial_balance

    def deposit(self,amount:int):
        self.initial_balance += amount
        return self.initial_balance

    def withdraw(self,amount:int):
        if amount> self.initial_balance:
            return f"The balance in your account is {self.initial_balance}, which is less than to complete your request"
        else:
            self.initial_balance -= amount
            return f"The balance after updating is {self.initial_balance}"
    def get_balance(self):
        return f"The current account balance is {self.initial_balance}"
    
    def get_account_holder(self):
        return f"The name of the account holder is {self.account_holder}"
        
#creating objects of class BankAccount
account1=BankAccount("amal",600)
account2=BankAccount("Ryoof",120000)

# calling the function (deposit)
print(account1.deposit(70))
print(account2.deposit(50000))

# calling the function (withdraw)
print(account1.withdraw(2000))
print(account2.withdraw(6000))

# calling the function (get_balance)
print(account1.get_balance())
print(account2.get_balance())

# calling the function (get_account_holder)
print(account1.get_account_holder())
print(account2.get_account_holder())

