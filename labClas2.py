
class BankAccount():

    def __init__(self,account_holder_name:str,intial_balance = 0.0):
        self.account_holder_name = account_holder_name
        self.intial_balance = intial_balance

    def get_balance(self):
        return self.intial_balance
    def get_account_hodler(self):
        return self.account_holder_name
    
    def deposit(self,balance:float):
        self.intial_balance += balance
        return self.intial_balance
    def withdraw(self,balance:float):
        if self.get_balance() == 0 or self.get_balance() - balance < 0:
            print(f"sorry not enough balance to withdraw from, here's your current balance: {self.intial_balance} ")
        else:
            print(self.get_balance())
            self.intial_balance -= balance
            print(self.get_balance())
        
    
BankAccount1 = BankAccount("Omar",10000)
BankAccount2 = BankAccount("Ahmed")
BankAccount3 = BankAccount("Moh",1000)

print(BankAccount1.get_balance())
print(BankAccount1.get_account_hodler())
print("--")
print(BankAccount2.get_balance())
print(BankAccount2.get_account_hodler())
print("--")
print(BankAccount3.get_balance())
print(BankAccount3.get_account_hodler())
print("--")

BankAccount1.deposit(1000)
print(BankAccount1.get_balance())
print("--")
#BankAccount2.deposit(10)
print(BankAccount2.get_balance())
print("--")
BankAccount3.deposit(30000000)
print(BankAccount3.get_balance())
print("--")
#BankAccount1.withdraw(250)
#BankAccount1.withdraw(300)
BankAccount1.withdraw(10000000000)
print("--")
BankAccount2.withdraw(100)



        