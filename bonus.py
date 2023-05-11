'''

'''
class Vehicle:

    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_number:str) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

#brand srtter & getter
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
         self.__brand = brand

#name srtter & getter
    def get_name(self):
        return self.__name

    def set_name(self, name):
         self.__name= name

#color srtter & getter
    def get_color(self):
        return self.__color

    def set_color(self, color):
         self.__color= color

#capacity srtter & getter
    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
         self.__capacity= capacity

#plate_number srtter & getter
    def get_plate_number(self):
        return self.__plate_number

    def set_plate_number(self, plate_number):
         self.__plate_number= plate_number


#vehicle methods    
    def drive(self):
        return(f"\nThe {self.get_name()} is driving!")

    def drift(self):
        return(f"\nThe {self.get_name()} is drifting!")

    def carry_cargo(self):
        return(f"\nThe {self.get_name()} is carrying cargo!\n")


class Bus(Vehicle):
    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_number:str) -> None:
        super().__init__(brand,name,color,capacity,plate_number)
        
    def drive(self):
        return super().drive()

    def drift(self):
        Vehicle.drift(self)
        return(f"\nThe {self.get_name()} bus cannot drift")

    def carry_cargo(self):
        Vehicle.carry_cargo(self)
        return(f"\nThe {self.get_name()} bus cannot carry a cargo\n")




class Truck(Vehicle):
    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_number:str) -> None:
        super().__init__(brand,name,color,capacity,plate_number)

    def drive(self):
        return super().drive()

    def drift(self):
        Vehicle.drift(self)
        return(f"\nThe {self.get_name()} cannot drift")

    def carry_cargo(self):
        Vehicle.carry_cargo(self)
        return(f"\nThe {self.get_name()} can carry a cargo\n")
    



vehicle1 = Bus("Mercedes","Tourismo", "Grey", 20,"MBT 350" )
print(vehicle1.drive())
print(vehicle1.drift())
print(vehicle1.carry_cargo())

vehicle2 = Truck("Volvo","Volvo truck","white",3,"VTW 652")
print(vehicle2.drive())
print(vehicle2.drift())
print(vehicle2.carry_cargo())