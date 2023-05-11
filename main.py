class BankAccount:
    def __init__(self,account_holder:str,initial_balance:float=0):
        self.account_holder=account_holder
        self._initial_balance=initial_balance
    
    def set_balance(self,set):
        if type(set) != float:
            raise ValueError("You must provide only number")

        if set < 0:
            raise ValueError(" provide an above 0  ")
        self._initial_balance = set
    
    def get_balance(self):
        return self._initial_balance
    
    def deposit(self,add):
       self._initial_balance+=add
       value=self._initial_balance
       return value
    
    def withdraw(self,sub):
        if self._initial_balance>=sub:
            self._initial_balance-=sub
            value=self._initial_balance
            return value
        else:
            return "you dont have money :("
        
account1=BankAccount("khalid")
print(account1.deposit(100))
print(account1.deposit(6700))
print(account1.withdraw(500))
print(account1.withdraw(100_000_000))

"""
output:
100
6800
6700
you dont have money :(
"""
    
            


 
        