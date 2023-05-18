#Exercise:

#Create a Python class called BankAccount that simulates a simple bank account. The class should have the following functionalities:

#It should have a constructor that accepts the account_holder name and initial balance (initial_balance), setting the balance to zero if the initial balance is not provided.
#A method called deposit that accepts an amount and adds it to the account balance, and then returns the updated balance.
#A method called withdraw that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
#A method called get_balance that returns the current account balance.
#A method called get_account_holder that returns the name of the account holder.



class BankAccount:
    def __init__(self, account_holder,inital_balance=0):
     
     self.account_holder = account_holder
     self.__inital_balance = inital_balance

     def deposit(self, amount):
        self.inital_balance += amount
        return self.inital_balance
     
     def withdraw(self, amount):
        if amount > self.inital_balance:
           raise Exception("you dont have enough funds")
           
        else:
           self.inital_balance -= amount
           return self.inital_balance
        
        def get_balance(self):
           return self.inital_balance
        
        def get_account_holder(self):
           return self.account_holder
        

        




#bouns:


class Vehicle:
 def __init__(self, brand, name, color, capacity, plate_number):
      self._brand = brand 
      self.name = name
      self._color = color 
      self._capacity = capacity
      self._plate_numper = plate_number

 def drifit(self):
    print(f"The {self._name}is driving !")

 def carry_cargo(self):
    print (f"The {self._name}is  carriyng cargo !!")

    property
    def set_brand(self, brand):
       return self._brand 
    
    def get_name(self):
       return self._name
    
    def set_color(self, color):
       return self._brand 
    
    def get_color(self):
       return self._color
    
    def set_caocity(self, caoacity):
       return self._brand 
    
    def get_capacity(self):
       return self._caoacity
    
    def plate_number(self, plate_number):
       return self._brand 
    
    def plate_nmuber(self, plate_number):
       return self._plate_number
    

    class Bus(Vehicle):
       

     def carry_cargo(self):
        print(f"the{self.get_name()}is carrying passengers !!")

    class Truck (Vehicle):
       
     def carry_cargo(self):
        print(f"the{self.get_name()}is carrting goods !!")



 




   