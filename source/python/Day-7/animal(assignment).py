from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Dog(Animal):
    def make_sound(self):
        print("bark")

class Cat(Animal):
    def make_sound(self):
        print("meow")

def main():
    d=Dog()
    d.make_sound()
    c=Cat()
    c.make_sound()
main()