from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,brand):
        self.brand=brand
    @abstractmethod
    def max_speed(self):
        pass

class Car(Vehicle):
    def max_speed(self):
        return "200kmh"
class Bike(Vehicle):
    def max_speed(self):
        return "150kmh"

c=Car("Audi")
b=Bike("BMW")
print(f"{c.brand} max speed:{c.max_speed()}")
print(f"{b.brand} max speed :{b.max_speed()}")