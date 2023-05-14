class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposit to your account")
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} has been withdrawen to your account")

            return self.balance
        else:
            print("Insufficient funds. Withdrawal canceled.")
            return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

account = BankAccount("MK")

account.deposit(500)
account.withdraw(700)
account.withdraw(200)

balance = account.get_balance()
account_holder = account.get_account_holder()

print("Account Holder:", account_holder)
print("Account Balance:", balance)
