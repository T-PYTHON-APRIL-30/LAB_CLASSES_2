# # Bonus

# ## define a Vehicle class . it has the following structure :

# #### properties attrabuite
# - brand
# - name
# - color
# - capacity
# - plate_number

class Vehicle:
    def __init__(self,brand:str,name:str,color:str,capacity, plate_number:int):

        self.brand= brand
        self.name = name
        self.color = color
        self.capacity = capacity
        self.plate_number = plate_number

# #### methods
# - drive()
#   prints "the vehicle_name is driving!"
    def drive(self):
        return f"the {self.name} is driving!"
    
# - drift()
#   prints "the vehicle_name is drifting !!" or something else depending on the class.
    def drift(self):
        return f"the {self.name} is drifting !!"
# - carry_cargo()
#   prints "the vehicle_name is carrying cargo !!" or something else depending on the class
    def carry_cargo(self):
        return f"the {self.name} is carrying cargo !!"


### for each of the properties do a setter & getter (encabsulate the data).

    #define a getter
    def get_brand(self):
        return self.__brand
    #define a setter
    def set_brand(self, brand):
        return self.__brand

    #define a getter
    def get_name(self):
        return self.__name
    #define a setter
    def set_name(self, name):
        return self.__name
    
    #define a getter
    def get_color(self):
        return self.__color
    #define a setter
    def set_color(self, color):
        return self.__color
    
        #define a getter
    def get_capacity(self):
        return self.__capacity
    #define a setter
    def set_capacity(self, capacity):
        return self.__capacity
    
        #define a getter
    def get_plate_number(self):
        return self.__plate_number
    #define a setter
    def set_plate_number(self, plate_number):
        return self.__plate_number



# ### Create tow other subclasses (inherit from vehicle):
# - Bus
# - Truck
class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity, plate_number: int,transfer:str):
        super().__init__(brand, name, color, capacity, plate_number)
        self.transfer = transfer

    def transfer_type1(self):
        return super().drive()+ f".It is has a special {self.color} color. the {self.name} bus can only transport the {self.transfer}.the capacity of {self.name} bus equal={self.capacity} seats"

class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity, plate_number:int,transfer):
        super().__init__(brand, name, color, capacity, plate_number)
        self.transfer = transfer

    def transfer_type2(self):
        return super().carry_cargo()+ f".It often a {self.color} color. the {self.name} truck can only transport the {self.transfer}.the capacity of {self.name} truck equal={self.capacity}m**3"




Vehicle_A = Vehicle(None,"Van","black",10,245)
Vehicle_B = Vehicle(None,"Car","white",7,609)
Vehicle_C = Vehicle(None,"Taxi","yellow",5,833)
Vehicle1 = Bus ("Wright Eclipse Gemini","London Transport","red","30",780,"people")
Vehicle2 = Truck ("Mercedes-Benz","ractor-trailer","grey",20,776,"products")

print(Vehicle_A.drive())
print(Vehicle_B.drift())
print(Vehicle_C.drive())
print(Vehicle1.transfer_type1())
print(Vehicle2.transfer_type2())



# ### Note
# - override  the methods as needed for each subclass of vehicle. 
# - create at least one object of each class.
# - call all the methods on each object. 
