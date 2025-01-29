#parent class
class shape:
    def area(self):
        pass

#child class 1
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius ** 2
    
#child class 2
class square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side * self.side
    
p=circle(4)
print(p.area())
q=square(2)
print(q.area())

