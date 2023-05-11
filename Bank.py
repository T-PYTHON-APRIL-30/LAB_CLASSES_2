"""# LAB_CLASSES_2

**Exercise:**

Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.
"""


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, amount: int):
        self.initial_balance += amount
        return self.initial_balance

    def withdraw(self, amount):
        if amount > self.initial_balance:
            print("Insufficient funds")
            return self.initial_balance
        else:
            self.initial_balance -= amount
            return self.initial_balance

    def get_balance(self):
        return self.initial_balance

    def get_account_holder(self):
        return self.account_holder


bank1 = BankAccount("BAkr", 1000)
print("money in the bank:")
print(bank1.initial_balance)
print("after depositthe money:")
print(bank1.deposit(500))
print("after withdraw:")
print(bank1.withdraw(250))
print("get account holder method:")
print(bank1.get_account_holder())
print("get money method")
print(bank1.get_balance())
