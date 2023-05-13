class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number) -> None:
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

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

    def get_plate_number(self):
        return self.__plate_number

