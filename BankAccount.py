'''
LAB_CLASSES_2
Exercise:

Create a Python class called BankAccount that simulates a simple bank account. The class should have the following functionalities:

It should have a constructor that accepts the account_holder name and initial balance (initial_balance), setting the balance to zero if the initial balance is not provided.
A method called deposit that accepts an amount and adds it to the account balance, and then returns the updated balance.
A method called withdraw that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
A method called get_balance that returns the current account balance.
A method called get_account_holder that returns the name of the account holder.
'''


class BankAccount:

    def __init__(self,account_holder:str,initial_balance:float=0):
        self.account_holder=account_holder
        self.initial_balance= initial_balance
#teacher solution
    def deposit(self, amount:float)-> float:
        #self.initial_balance+=amount
        #return self.initial_balance
        updated_balance = amount+ self.get_balance()
        self.initial_balance= updated_balance
        print("The process was successfully")
        return updated_balance

    def withdraw (self, amount:float)->float:
        if amount > self.get_balance():
            #raise Exception("You don't have enough funds !")
            print("The amout is out of your balane")
        #else:
        #self.initial_balance-=amount
        #return self.initial_balance
        updated_balance= self.get_balance()-amount
        self.initial_balance= updated_balance
        print("The process was successfully")
        return updated_balance

    def get_balance(self):
        return self.initial_balance

    def get_account_holder(self):
        return self.account_holder
    
    #Set functions
    '''def set_balance(self, balance:float):
        if type(balance) != float:
            raise ValueError("You must provide a valid balance")
        self.__initial_balance =balance

    def set_account_holder(self, name:str):
        if type(name) != str:
            raise ValueError("You must provide a valid name")
        self.__account_holder=name'''

account_holder1= BankAccount("Fahad",5000)
account_holder2= BankAccount("Noura",2000)

print(account_holder1.get_account_holder())

user_input= float(input("The amount to be deposited? "))
print(f"The updated balance : {account_holder1.deposit(float(user_input))}")
user_input2=float(input("The amount to be withdrawn? "))
print(f"The updated balance : {account_holder1.withdraw(user_input2)}")

print(account_holder1.get_balance())

