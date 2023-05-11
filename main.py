# ----------- LAB_CLASSES_2 -----------
print("---------------------- LAB_CLASSES_2 ----------------------\n")

class BankAccount():
    def __init__(self , account_holder : str, initial_balance:float = 0 ) :
        self.account_holder = account_holder
        self.initial_balance = initial_balance
    
    def deposit(self,amount:float):
        self.initial_balance += amount
        return self.initial_balance
    
    def withdraw(self,amount:float):
        if amount <= self.initial_balance:
            self.initial_balance -= amount
            return self.initial_balance
        else:
            return print("Your balance not allowed to withdraw.")
    
    def get_balance(self):
        return self.initial_balance
    
    def get_account_holder(self):
        return self.account_holder
print("- _"*19)
print("- _ - _ - _ - _ - Welcome To Python Bank - _ - _ - _ - _ - . ") 
print("_ -"*19)
print("\nPLease fill the following requirements:-")
userName = str(input("Enter your fist name * : "))
userBalance = float(input("Enter your courrnet balance * : "))
account1 = BankAccount(userName,userBalance)

while True:
    print("\nWhat is the opreation that you want to do ?")
    userInput = str(input("\n[ Name the account holder ( n ) - Show amount ( s ) - Deposit amount ( d ) - Withdraw amount ( w ) ]\n\nExit ( e )\n\nEnter: "))
    if not userInput.isdigit() and len(userInput) == 1 :
        
        if userInput == "n" :
            print(f"\nThe account holder is:\n\n\t{account1.get_account_holder()}")    
        elif userInput == "s" :
            print(f"\nYour currnet balance is:\n\n\t{round((account1.get_balance()),2)}")
        elif userInput == "d" :
            amountDeposite = float(input("\nEnter the amount that you want to deposit it:"))
            account1.deposit(amountDeposite)
            print()
        elif userInput == "w" :
            amountWithdraw = float(input("\nEnter the amount that you want to withdraw it:"))
            account1.withdraw(amountWithdraw)
            print()
        elif userInput == "e" :
            print(f"\nGood bye {account1.get_account_holder()} :)")
            break
        else:
            print("\nWrong entry.. Try again !")
    else:
        print("\nWrong entrt.. Try again !")