'''Create a Python class called BankAccount that simulates a simple bank account. The class should have 
the following functionalities:

It should have a constructor that accepts the account_holder name and initial balance (initial_balance),
 setting the balance to zero if the initial balance is not provided.
A method called deposit that accepts an amount and adds it to the account balance, 
and then returns the updated balance.
A method called withdraw that accepts an amount and subtracts it from the account balance,
 returning the updated balance, but only if there are sufficient funds in the account.
   If there are insufficient funds, it should print an error message and leave the balance unchanged.
A method called get_balance that returns the current account balance.
A method called get_account_holder that returns the name of the account holder.'''

class BankAccount:
    
    def __init__(self, account_holder: str, initial_balance : float = 0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, amount:float)-> float:

        self.initial_balance += amount

        return self.initial_balance
    
    def withdraw (self, amount:float)-> float:
        
        if amount <= self.initial_balance:
            self.initial_balance -= amount
        
        else:
            raise Exception('there are insufficient funds!!')
            
        return self.initial_balance
        
    
    def getBalance(self)-> float:
        return self.initial_balance
    

    def get_account_holder(self):
        return self.account_holder
    

account1 = BankAccount('Amani',500000.0)
balance = account1.deposit(10000.0)
print(f'Your balance after the deposit is: {balance}')
balance = account1.withdraw(5000.0)
print(f'Your balance after the withdraw is: {balance}')
print(f'The account holder is {account1.account_holder}')
print(f'The initial balance is: {account1.initial_balance}')

    
