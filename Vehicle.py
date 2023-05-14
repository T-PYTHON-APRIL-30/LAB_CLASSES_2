'''efine a Vehicle class . it has the following structure :
methods
drive() prints "the vehicle_name is driving!"
drift() prints "the vehicle_name is drifting !!" or something else depending on the class.
carry_cargo() prints "the vehicle_name is carrying cargo !!" or something else depending on the class
for each of the properties do a setter & getter (encabsulate the data).
Create tow other subclasses (inherit from vehicle): Bus and Truck
Note:
override the methods as needed for each subclass of vehicle.
create at least one object of each class.
call all the methods on each object.'''

class Vehicle:

    def __init__(self, brand:str, name:str, color:str, capacity:int, plateNumber:str):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plateNumber = plateNumber


    def drive(self):
        print(f'The {self.getName()} is driving..')
    
    def drift(self, checkValue:bool)-> str:
        if checkValue == True:
            return f'The {self.getName()} is drifting..'
        else:
            return f'The {self.getName()} is not drifting..'

    def carryCarg(self,checkValue:bool):
        if checkValue == True:
            return f'The {self.getName()} is carrying cargo..'
        
        else:
            return f'The {self.getName()} is not carrying cargo..'

    def getBrand(Self):
        return Self.__brand
    
    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color
    
    def getCapacity(self):
        return self.__capacity
    
    def getPlateNumber(self):
        return self.__plateNumber
    
    def setBrand(self,carBrand:str):
        if type(carBrand) != str:
            raise ValueError('Please provide a valid value!!')
        
        self.__brand = carBrand

    def setName(self, carName:str):
        if type(carName) != str:
            raise ValueError('Please provide a valid value!!')
        
        self.__name = carName

    def setColor(self, carColor:str):
        if type(carColor) != str:
            raise ValueError('Please provide a valid value!!')
        
        self.__color = carColor

    def setCapacity(self,carCapacity:int):
        if type(carCapacity) != int:
            raise ValueError('Please provide a valid value!!')
        
        self.__capacity = carCapacity
    
    def setPlateNumber(self, carPlateNumber:str):
        if type(carPlateNumber) != str:
            raise ValueError('Please provide a valid value!!')
        
        self.__plateNumber = carPlateNumber


class Bus (Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plateNumber: str, drifting:bool = False, hasCargo: bool = False):
        super().__init__(brand, name, color, capacity, plateNumber)
        self.drifting = drifting
        self.hasCargo = hasCargo

    
    def carryCarg(self):
        return super().carryCarg(self.getHasCargo())
    
    def drift(self):
        return super().drift(self.getDrifting())
    
    def drive(self):
        return super().drive()
    
    def getHasCargo(self):
        return self.hasCargo
    
    def getDrifting(self):
        return self.drifting
    


class Truck(Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plateNumber: str, drifting:bool = True, hasCargo: bool = True):
        super().__init__(brand, name, color, capacity, plateNumber)
        self.__drifting = drifting
        self.__hasCargo = hasCargo

    def carryCarg(self):
        return super().carryCarg(self.getHasCargo())
    
    def drift(self):
        return super().drift(self.getDrifting())
    
    def drive(self):
        return super().drive()
    
    def getHasCargo(self):
        return self.__hasCargo
    
    def getDrifting(self):
        return self.__drifting
    



vehicle1 = Vehicle('BMW','7 series', 'Black', 4, '1 AAA')
vehicle1.drive()
print(vehicle1.drift(True))
print(vehicle1.carryCarg(True))
print()

bus1 = Bus('Hilux','Van','White',8, '123 asd')
bus1.drive()
print(bus1.drift())
print(bus1.carryCarg())
print()

truck1 = Truck('GMC','Sierra','Gray',4,'444 fff')
truck1.drive()
print(truck1.drift())
print(truck1.carryCarg())
print()