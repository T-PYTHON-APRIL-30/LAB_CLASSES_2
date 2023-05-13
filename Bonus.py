'''define a Vehicle class . it has the following structure :
properties
brand
name
color
capacity
plate_number
methods
drive() prints "the vehicle_name is driving!"
drift() prints "the vehicle_name is drifting !!" or something else depending on the class.
carry_cargo() prints "the vehicle_name is carrying cargo !!" or something else depending on the class
for each of the properties do a setter & getter (encabsulate the data).
Create tow other subclasses (inherit from vehicle):
Bus
Truck
Note
override the methods as needed for each subclass of vehicle.
create at least one object of each class.
call all the methods on each object.
'''

class Vehicle:

    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_number:str):
        self.__brand = brand
        self.__name = name
        self.__color =color
        self.__capacity= capacity
        self.__plate_number=plate_number
    
    #methods
    def drive(self, name):
        print(f"the {self.get_name()} is driving!")

    def drift(self, name):
        print(f"the {self.get_name()} is drifting !!")

    def carry_cargo(self,name):
        print(f"the {self.get_name()} is carrying cargo !!")

    
    #setter & getter (brand)
    def get_brand(self):
        return self.__brand
    def set_brand(self, brand):
        if type(brand) != str:
            raise ValueError("You must provide a valid value!")
        self.__brand=brand

    #setter & getter (name)
    def get_name(self):
        return self.__name
    def set_name(self, name):
       if type(name) != str:
            raise ValueError("You must provide a valid value!") 
       self.__name=name

    #setter & getter (color)
    def get_color(self):
        return self.__color
    def set_color(self, color):
        if type(color) != str:
            raise ValueError("You must provide a valid value!") 
        self.__color=color

    #setter & getter (capacity)
    def get_capacity(self):
        return self.__capacity
    def set_capacity(self, capacity):
        if type(capacity) != int:
            raise ValueError("You must provide a valid value!") 
        self.__capacity=capacity

    #setter & getter (palte number)
    def get_plate_number(self):
        return self.__plate_number
    def set_plate_number(self, plate_number):
        if type(plate_number) != str:
            raise ValueError("You must provide a valid value!") 
        self.__plate_number=plate_number


#Bus class 
class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str):
        super().__init__(brand, name, color, capacity, plate_number)

    def drive(self, name):
        return super().drive(name)

    def drift(self, name: str):
        return f"the {self.get_name()} isn't drifting!"
    
    def carry_cargo(self, name: str):
        return f"the {self.get_name()} isn't carrying cargo !!"
    
bus1=Bus("Mercedes", "Mercedes Benz Bus", "Silver", 13, "123-ABC")
print(bus1.drive(bus1.get_name()))
print(bus1.drift(bus1.get_name()))
print(bus1.carry_cargo(bus1.get_name()))
print("\n")


#Trick class
class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str):
        super().__init__(brand, name, color, capacity, plate_number)

    def drive(self, name):
        return super().drive(name)
    
    def drift(self, name):
        return f"the {self.get_name()} isn't drifting!"
    
    def carry_cargo(self, name):
        return super().carry_cargo(name)
    

truck1=Truck("Volvo","Volvo Truck96","blue", 45, "567-FGH")

print(truck1.drive(truck1.get_name()))
print(truck1.drift(truck1.get_name()))
print(truck1.carry_cargo(truck1.get_name()))

