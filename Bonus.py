
class Vehicle():
    def __init__(self,brand:str,name:str,color:str,capacity:int,plate_number:str):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        return f"the {self.__name} is driving"
    def drifting(self):
        return f"the {self.__name} is drifting"
    def carry_cargo(self):
        return f"the {self.__name} is carrying cargo"

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
    

class bus(Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str,type:str):
        super().__init__(brand, name, color, capacity, plate_number)
        self.__type = type

    def get_type(self):
        return self.__type
    def set_type(self,type):
        self.__type = type

    def drive(self):
        return super().drive() + f" here's my type: {self.__type}"
    def drifting(self):
        return super().drifting() + f" here's my type: {self.__type}"
    def carry_cargo(self):
        return super().carry_cargo() + f" here's my type: {self.__type}"
    
class truck(Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str, size:str):
        super().__init__(brand, name, color, capacity, plate_number)
        self.__size = size
    def get_size(self):
        return self.__size
    def set_size(self,size):
        self.__size = size

    def drive(self):
        return super().drive() + f" here's my type: {self.__size}"
    def drifting(self):
        return super().drifting() + f" here's my type: {self.__size}"
    def carry_cargo(self):
        return super().carry_cargo() + f" here's my type: {self.__size}"
    



Vehicle1 = Vehicle("bmw","skyline","black",4,"GHR-234")
bus1 = bus("mercedes","neon","yellow",14,"FFF-123","School bus")
truck1 = truck("toyota","monster","green",2,"VMK-678","VERY LARGE")
    
print(Vehicle1.get_brand())
print(Vehicle1.get_capacity())
print(Vehicle1.drive())
print(Vehicle1.drifting())
print(Vehicle1.carry_cargo())

print("--")

print(bus1.get_color())
print(bus1.get_name())
print(bus1.get_type())
print(bus1.drive())
print(bus1.drifting())
print(bus1.carry_cargo())

print("--")


print(truck1.get_plate_number())
print(truck1.get_size())
print(truck1.drive())
print(truck1.drifting())
print(truck1.carry_cargo())