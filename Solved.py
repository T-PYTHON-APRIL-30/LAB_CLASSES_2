class BankAccount:
    

    initial_balance = 0
    
    def __init__(self,account_holder:str, initial_balance:int=0) -> None:
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, add_amount):
        
        self.initial_balance += add_amount
        return f"the new balance is {self.initial_balance}"
    
    def withdraw(self,withdraw_amount):

            if self.initial_balance >= withdraw_amount:
                
                self.initial_balance -= withdraw_amount
                return f"the new balance is {self.initial_balance}"

            else:
                print("Balance is not allowed!!")

    def get_balance(self):
        print(f"current balance is: {self.initial_balance}")

    def get_account_holder(self):
        print(f"name of account holder is: {self.account_holder}")

process_info = BankAccount

try:
    process_info = BankAccount(account_holder= str(input("Name of account holder: ")), initial_balance= int(input("How much the balance: ")))
except:
    process_info.initial_balance = 0

try:
    print(process_info.deposit(int(input("how much you want to add? "))))
except:
    pass

try:
    print(process_info.withdraw(int(input("how much you want to withdraw? "))))
except:
    pass


print(process_info.get_balance())
print(process_info.get_account_holder())
