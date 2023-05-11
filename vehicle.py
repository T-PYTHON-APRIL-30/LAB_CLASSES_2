"""
## define a Vehicle class . it has the following structure :

#### properties
- brand
- name
- color
- capacity
- plate_number


#### methods
- drive()
  prints "the vehicle_name is driving!"
- drift()
  prints "the vehicle_name is drifting !!" or something else depending on the class.
- carry_cargo()
  prints "the vehicle_name is carrying cargo !!" or something else depending on the class


### for each of the properties do a setter & getter (encabsulate the data).

### Create tow other subclasses (inherit from vehicle):
- Bus
- Truck


### Note
- override  the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object. 
"""


class Vehicle:
    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_number:str):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        print(f"the {self.__name} is driving!")

    def drift(self):
        print(f"the {self.__name} is drifting !!")

    def carry_cargo(self):
        print(f"the {self.__name} is carrying cargo !!")

# getters and setters for each property
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_plate_number(self):
        return self.__plate_number

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number


class Bus(Vehicle):
    def drive(self):
        print(f"The {self.get_name()} bus is driving!")

    def drift(self):
        print(f"The {self.get_name()} bus cannot drift.")

    def carry_cargo(self):
        print(f"The {self.get_name()} bus is carrying passengers!")


class Truck(Vehicle):
    def drive(self):
        print(f"The {self.get_name()} truck is driving!")

    def drift(self):
        print(f"The {self.get_name()} truck cannot drift.")

    def carry_cargo(self):
        print(f"The {self.get_name()} truck is carrying good!")

# create objects of each class
my_vehicle = Vehicle("Dodge", "challenger", "Red", 4, "BKR444")
my_bus = Bus("Mercedes", "V-class", "silver", 50, "DEF456")
my_truck = Truck("Ford", "F-150", "Blue", 100, "PYT000")

# call all methods on each object
print(my_vehicle.get_brand())
my_vehicle.drive()
my_vehicle.drift()
my_vehicle.carry_cargo()
print("")
print(my_bus.get_brand())
my_bus.drive()
my_bus.drift()
my_bus.carry_cargo()
print("")
print(my_truck.get_brand())
my_truck.drive()
my_truck.drift()
my_truck.carry_cargo()