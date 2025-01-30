from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b
    
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14 * self.r ** 2
    
def main():
    r=Rectangle(2,3)
    c=circle(4)
    print(r.area())
    print(c.area())
main()
