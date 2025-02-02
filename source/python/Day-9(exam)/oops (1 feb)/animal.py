class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("the animal is speaking")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("the dog is making sound")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("the cat is making sound")

def main():
    c=Cat("rose")
    c.speak()
main()