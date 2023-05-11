class BankAccount:
    def __init__(self,account_holder:str,initial_balance:float):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit (self,amount):
        print("Your balance before the deposit is ",self.initial_balance)
        self.initial_balance += amount
        print("Your balance after the deposit is ",self.initial_balance)

    def withdraw (self,amount):
        print("Your balance before the withdraw is ",self.initial_balance)
        if self.initial_balance >= amount:
            self.initial_balance -= amount
            print("Your current balance after the withdraw is ",self.initial_balance)

        else :
            print("The number you are withdrawing is more than your current account balance")
    def get_balance (self):
        return self.initial_balance
    def get_account_holder (self):
        return self.account_holder

user1 = BankAccount(input("Enter user name: "),int(input("Enter the intial value: ")or 0))

user1.deposit(float(input("how much do you want to deposit? ")))

user1.withdraw(float(input("how much do you want to withdraw? ")))

print(user1.get_balance())

print(user1.get_account_holder())