class Vehicle:
    def __init__(self, properties: str, brand: str, name: str, color: str, capacity: int, plate_number: str):
        self.__properties = properties
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    

    def drive(self):
        return print(f"the {self.get_name()} is driving!")
    def drift(self):
        return print(f"the {self.get_name()} is drifting !!")
    def carry_cargo(self):
        return print(f"the {self.get_name()} is carrying cargo !!")
    

    def get_properties(self):
        return self.__properties
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
    

    def set_properties(self, properties):
        if len(properties) > 10:
            raise ValueError("Enter a known properties pleas...")
        self.__properties = properties
    def set_brand(self, brand):
        if len(brand) > 10:
            raise ValueError("Enter a known brand pleas...")
        self.__brand = brand
    def set_name(self, name):
        if len(name) > 10:
            raise ValueError("Enter a known name pleas...")
        self.__name = name
    def set_color(self, color):
        if len(color) > 10 or color.isalpha() == False:
            raise ValueError("Enter a known color pleas...")
        self.__color = color
    def set_capacity(self, capacity):
        if capacity > 9 or type(capacity) != int:
            raise ValueError("The capacity has be less than 9 seats...")
        self.__capacity = capacity
    def set_plate_number(self, plate_number):
        if len(plate_number) > 7:
            raise ValueError("The plate number has be less than 7 characters...")
        self.__plate_number = plate_number


class Bus(Vehicle):
    def __init__(self, properties, brand, name, color, capacity, plate_number):
        super().__init__(properties, brand, name, color, capacity, plate_number)
    

    def drift(self):
        return print(f"the {self.get_name()} is hurrying !!")
    def carry_cargo(self):
        return print(f"the {self.get_name()} is carrying students !!")


class Truck(Vehicle):
    def __init__(self, properties, brand, name, color, capacity, plate_number):
        super().__init__(properties, brand, name, color, capacity, plate_number)
    

    def drift(self):
        return print(f"the {self.get_name()} is digging !!")
    def carry_cargo(self):
        return print(f"the {self.get_name()} is carrying Bricks !!")


vehicle = Vehicle("Yousef", "MAZDA", "M3", "Black", 5, "ysf612")
bus = Bus("Mohammed", "Toyota", "asd123", "Yellow", 9, "mhmd123")
truck = Truck("Abdallah", "Marseds", "dsa321", "Brown", 2, "abod321")

vehicle.drive()
vehicle.drift()
vehicle.carry_cargo()

bus.drive()
bus.drift()
bus.carry_cargo()

truck.drive()
truck.drift()
truck.carry_cargo()