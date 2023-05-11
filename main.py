class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance


    def deposit(self, amount: float):
        self.initial_balance += amount
        return print(f"Your Amount know is {self.initial_balance} SAR")


    def withdraw(self, amount: float):
        if amount <= self.initial_balance:
            self.initial_balance -= amount
            return print(f"Your Amount know is {self.initial_balance} SAR")
        else:
            raise ValueError(f"The amount is not allowed. your amount is {self.initial_balance} SAR")


    def get_balance(self):
        return print(f"You have {self.initial_balance} SAR")


    def get_account_holder(self):
        return print(self.account_holder)


user_input = BankAccount("Yousef")

user_input.get_account_holder()
user_input.get_balance()
user_input.deposit(1000000)
user_input.withdraw(1)