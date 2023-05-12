class Vehicle:
    def __init__(self, brand:str,name:str, color:str, capacity:int,plate_number:int) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number



    def drive(self):
        return f"the {self.__name} is driving!"
    def drift(self):
        return f"the {self.__name} is drifting !!"
    def carry_cargo(self):
        return f"the {self.__name} is carrying cargo !!"
    #for each of the properties do a setter & getter (encabsulate the data).
    def get_pro(self):
        return self.__brand,self.__name
    def set_pro(self,new_brand,new_name):
        self.__name = new_name
        self.__brand = new_brand

car1 = Vehicle("Tesla","Roadster", "Plack", 40,7575)
print(car1.drive())
print(car1.drift())
print(car1.carry_cargo())
print(f"The color of the car is{car1.__color}")
print(car1.get_pro())
car1.set_pro("Tesla0","RostNew")
print(car1.get_pro())


class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

    def drive(self):
        return super().drive()
    def drift(self):
        return super().drift()
    def carry_cargo(self):
        return super().carry_cargo()
    def set_pro(self,new_brand,new_name):
        return super().set_pro(new_name,new_brand)
    def get_pro(self):
        return super().get_pro()
    
car2 = Bus("BMW","i7", "Red",12,1221)
print(car2.drive())
print(car2.drift())
print(car2.carry_cargo())
print(car2.get_pro())
car2.set_pro("Ji","BMW1")
print(car2.get_pro())



class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

    def drive(self):
        return super().drive()
    def drift(self):
        return super().drift()
    def carry_cargo(self):
        return super().carry_cargo()
    def set_pro(self,new_brand,new_name):
        return super().set_pro(new_name,new_brand)
    def get_pro(self):
        return super().get_pro()
    
car3 = Bus("Chevrolet","Z06", "Yello", 70,1111)
print(car3.drive())
print(car3.drift())
print(car3.carry_cargo())
print(car3.get_pro())
car3.set_pro("i75","Chevro0")
print(car3.get_pro())

