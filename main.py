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

#--------------- Bonus ---------------

class Vehicle():

    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:str):
        self.brand = brand
        self.name = name 
        self.color = color
        self.capacity = capacity
        self.__plate_number = plate_number
    
    def get_plate_number(self):
        return self.__plate_number
    def set_plate_number(self,plate_number):
        self.__plate_number = plate_number
        

    def drive(self):
        return f"The {self.name} is driving!"
    def drift(self):
        return f"The {self.name} is drifting !!"
    def carry_cargo(self):
        return f"The {self.name} is carrying cargo !!"

class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int,fuel:str, plate_number: str,catagory:str):
        super().__init__(brand, name, color, capacity, plate_number)
        self.fuel = fuel
        self.catagory = catagory
    def busFuel (self):
        return f"it is {self.fuel}"
    def carry_cargo(self):
        return f"The {self.name} its for {self.catagory}"
    

class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int,fuel:str, plate_number: str,wheel:int):
        super().__init__(brand, name, color, capacity, plate_number)
        self.fuel = fuel
        self.wheel = wheel
    def drift(self):
        return f" so the {self.name} It's drift hardly !!"
    def truckFuel (self):
        return f"it is {self.fuel}"
    def carry_cargo(self):
        return super().carry_cargo() + f"{self.drift()}"


myTruck = Truck("Mercedes","Actros","blue",11554,"diesel","Yz97c",10)
myBus = Bus("Toyota","Hiace","white",2275,"petrol","wx123","freight")


print("---- Bus ----\n")
print(myBus.drive() +"\n"+myBus.carry_cargo() + " and " + myBus.busFuel()+".")
print(f"Also its color It's {myBus.color} and is plate number is {myBus.get_plate_number()}.")
print("\n---- Truck ----\n")
print(f"The {myTruck.name} It's made by {myTruck.brand} with {myTruck.wheel} wheels.")
print(myTruck.carry_cargo() + " and " + myTruck.truckFuel()+".")
print(f"Also its color It's {myTruck.color} and is plate number is {myTruck.get_plate_number()}.")

# capacity
print("\n---- Comparison capacity ----\n")
if myBus.capacity > myTruck.capacity:
    print(f"The {myBus.name} has more capacity than {myTruck.name}.")
elif myBus.capacity < myTruck.capacity:
    print(f"The {myTruck.name} has more capacity than {myBus.name}.")
else:
    print(f"The {myBus.name} and the {myTruck.name} has the same capacity.")