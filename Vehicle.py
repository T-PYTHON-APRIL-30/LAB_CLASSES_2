# Bonus
from typing import Any


class Vehicle:
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        return f"{self.__name} is driving!"

    def drift(self):
        return f"{self.__name} is drifting !!"

    def carry_cargo(self):
        return f"{self.__name} is carrying cargo !!"

    # getters and setters
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

    def set_brand(self, brand):
        self.__brand = brand

    def set_brand(self, name):
        self.__name = name

    def set_brand(self, color):
        self.__color = color

    def set_brand(self, capacity):
        self.__capacity = capacity

    def set_brand(self, plate_number):
        self.__plate_number = plate_number


class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int):
        super().__init__(brand, name, color, capacity, plate_number)

    def drive(self):
        return super().drive() + f" it can carry up to " + str(super().get_capacity()) + " people"


class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int, load_capacity: int):
        super().__init__(brand, name, color, capacity, plate_number)
        self.load_capacity = load_capacity

    def carry_cargo(self):
        return super().carry_cargo() + f" it is about {self.load_capacity} pounds"


vehicle1 = Vehicle("Ford", "Grand Marquis", "Silver", 4, 21)
bus1 = Bus("Marcopolo", "Paradiso G8 1800 DD", "Blue", 50, 4856)
truck1 = Truck("Western Star", "49X", "red", 2, 9317, 50000)

print(vehicle1.drift())
print(truck1.carry_cargo())
print(bus1.drive())
