# LAB_CLASSES_2

'''**Exercise:**

Create a Python class called `BankAccount` that simulates a simple bank account. 
The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` 
name and initial balance (`initial_balance`), setting the balance to zero if 
the initial balance is not provided.

2. A method called `deposit` that accepts an amount and adds it to the account
 balance, and then returns the updated balance.

3. A method called `withdraw` that accepts an amount and subtracts it from the 
account balance, returning the updated balance, but only if there are sufficient 
funds in the account. If there are insufficient funds, it should print an error 
message and leave the balance unchanged.

4. A method called `get_balance` that returns the current account balance.

5. A method called `get_account_holder` that returns the name of the account holder.

---------'''


class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, new_deposit):
        self.initial_balance = self.initial_balance + new_deposit
        return (f"Hello {self.account_holder} your new balance is: {self.initial_balance}")

    def withdraw(self, new_withdraw):
        if new_withdraw > self.initial_balance:
            return (print("insufficient funds"))
        else:
            self.initial_balance = self.initial_balance-new_withdraw
            return (f"Hello {self.account_holder} your new balance is: {self.initial_balance}")

    def get_balance(self):
        return (f"your account balance is: {self.initial_balance}")

    def get_account_holder(self):
        return (self.account_holder)

person1 = BankAccount("Ahmed", 1500)
person2 = BankAccount("Abdullah", 0)
'''value=0
print("Welcome to my bank how can I help you today: ")
choices=int(input("Enter 1 to deposit: "))
if choices==1:
    input("how much do you want to deposit: ",person1.deposit(value))
'''

print(person1.deposit(1500))
print(person1.withdraw(20000))
print(person1.get_account_holder())
print(person1.get_balance())

print(person2.deposit(1500))
print(person2.withdraw(1000))
print(person2.get_account_holder())
print(person2.get_balance())