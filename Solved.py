class BankAccount:
   
    
    def __init__(self,account_holder:str, initial_balance = 0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, add_amount:int):
        
        self.initial_balance += add_amount
        return f"the new balance is {self.initial_balance}"
    
    def withdraw(self,withdraw_amount:int):

            if self.initial_balance >= withdraw_amount:
                
                self.initial_balance -= withdraw_amount
                return f"the new balance is {self.initial_balance}"

            raise ValueError("Balance is not allowed!!")

    def get_balance(self):
        print(f"current balance is: {self.initial_balance}")

    def get_account_holder(self):
        print(f"name of account holder is: {self.account_holder}")
        

process_info = BankAccount(account_holder = str(input("Name of account holder: ")))

try:
    process_info.initial_balance = int(input("How much the initial balance: "))
except:
    process_info.initial_balance = 0

try:
    print(process_info.deposit(int(input("how much you want to add? "))))
except:
    pass

try:
    print(process_info.withdraw(int(input("how much you want to withdraw? "))))
except Exception as e:
    print(e)


print(process_info.get_balance())
print(process_info.get_account_holder())
