class vechile:
    def __init__(self,type):
        self.type=type
    def display(self):
        print(f"vechile type is {self.type}")

class car(vechile):
    def __init__(self, name):
        self.name=name
    def display(self):
        print(f"The name of the car is : {self.name}")

class bike(vechile):
    def __init__(self, name):
        self.name=name
    def display(self):
        print(f"The name of the bike is : {self.name}")

class electricCar(car):
    def display(self):
        print(f"The name of the electric car is {self.name}")

def main():
    v=vechile("type is car")
    v.display()
    c=car("audi")
    c.display()
    b=bike("bmw")
    b.display()
    e=electricCar("tesla")
    e.display()
main()