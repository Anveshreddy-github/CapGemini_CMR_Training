class car:
    def move(self):
        return "car is moving"

class airplane:
    def move(self):
        return "airplane is flying"

class flycar(car,airplane):
    def move(self):
        print(f"flying car is combination of both {car.move(self)} and {airplane.move(self)}")


def main():
    f=flycar()
    f.move()
main()