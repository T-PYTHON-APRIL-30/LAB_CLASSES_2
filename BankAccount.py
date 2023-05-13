class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0) -> None:
        self.__acount_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("please write positive number for amount")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("please write positive number for amount")
        if self.balance < amount:
            raise ValueError("have not balance enough")
        self.__balance -= amount
        raise self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__acount_holder
