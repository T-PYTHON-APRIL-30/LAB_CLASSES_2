import Vehicle
class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number, passengers_number) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.passengers_number = passengers_number