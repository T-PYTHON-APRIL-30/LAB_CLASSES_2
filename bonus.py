class Vehicle:
    def __init__(self,brand,name,color,capacity,plate_number):
        self._brand=brand
        self._name=name
        self._color=color
        self._capacity=capacity
        self._plate_number=plate_number
    def drive(self):
        return print(f"the {self._name} is driving!")
    def drift(self):
        return print(f'the {self._name} is drifting !!')
    def carry_cargo(self):
        return print(f"the {self._name} is carrying cargo !!")
    
    def set_brand(self,setter):
        self._brand=setter
        return setter
    def set_name(self,setter):
        self._name=setter
        return setter
    def set_color(self,setter):
        self._color=setter
        return setter
    def set_capacity(self,setter):
        self._capacity=setter
        return setter
    def set_plate_number(self,setter):
        self._plate_number=setter
        return setter
    
    def get_brand(self):
        return self._brand
    def get_name(self):
        return self._name
    def get_color(self):
        return self._color
    def get_capacity(self):
        return self._capacity
    def get_plate_number(self):
        return self._plate_number
    

class Bus(Vehicle):
        def __init__(self, brand, name, color, capacity, plate_number,size):
            super().__init__(brand,name,color,capacity,plate_number)
            self.size=size

        def drive(self):
            return print(f"the {self._name} bus is driving!")
        def drift(self):
            return print(f'the {self._name} bus is drifting !!')
        def carry_cargo(self):
            return print(f"the {self._name} bus is carrying cargo !!")
    
        
class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number,truck_model):
        super().__init__(brand,name,color,capacity,plate_number)
        self.truck_model=truck_model

    def drive(self):
        return print(f"the {self._name} truck is driving!")
    def drift(self):
        return print(f'the {self._name} truck is drifting !!')
    def carry_cargo(self):
        return print(f"the {self._name} truck is carrying cargo !!")


Vehicle1=Vehicle("ford","explorer","white",8,3944)
Vehicle1.drive()
Vehicle1.drift()
Vehicle1.carry_cargo()

bus1=Bus("mercedes","FLX-500","white",32,1235,15)
bus1.drive()
bus1.drift()
bus1.carry_cargo()

Truck1=Truck("ford","F-150","blue",4,5789,"2015")
Truck1.drive()
Truck1.drift()
Truck1.carry_cargo()


    





    
      


      