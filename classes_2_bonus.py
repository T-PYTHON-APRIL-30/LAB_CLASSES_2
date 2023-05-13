#define a Vehicle class.
class Vehicle :
    def __init__(self,brand:str,name:str,color:str,capacity:float,plate_number:int):
        #it has the following structure
        self.__brand= brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    #getters (encabsulate the data)
    def get_brand(self):
        return self.__brand
    def get_name(self):
        return self.__name
    def get_color(self):
        return self.__color
    def get_capacity(self):
        return self.__capacity
    def get_plate_number(self):
        return self.__plate_number
    
    #setters (encabsulate the data)
    def set_brand(self,brand):
        self.__brand = brand
    def set_name(self,name):
        self.__name = name
    def set_color(self,color):
        self.__color = color
    def set_capacity(self,capacity):
        self.__capacity = capacity
    def set_plate_number(self,plate_number):
        self.__plate_number = plate_number
    
    #methods
    def drive (self):
        print (f"the {self.get_name()} is driving!")
    
    def drift (self):
        print (f"the {self.__name} is drifting!!")
    
    def carry_cargo (self):
        print (f"the {self.__name} is carrying a cargo!!")

#Create tow other subclasses (inherit from vehicle)
class Bus (Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: float, plate_number: int,seat_number:int):
        super().__init__(brand, name, color, capacity, plate_number)    
        self.seat_number = seat_number

#Create tow other subclasses (inherit from vehicle)
class Truck (Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: float, plate_number: int,torque:float):
        super().__init__(brand, name, color, capacity, plate_number)
        self.torque = torque

#create at least one object of each class.
vehicle1 = Vehicle("GMC","suberban","black",90,1)
vehicle2 = Truck("GMC","Sieera","black",90,2,460)
vehicle3 = Bus("GM","transit","Yellow and black",140,3,40)

#call all the methods on each object.
print(f"{vehicle1.drift()}\n{vehicle1.drive()}\n{vehicle1.carry_cargo()}")
print(f"{vehicle2.drift()}\n{vehicle2.drive()}\n{vehicle2.carry_cargo()}")
print(f"{vehicle3.drift()}\n{vehicle3.drive()}\n{vehicle3.carry_cargo()}")