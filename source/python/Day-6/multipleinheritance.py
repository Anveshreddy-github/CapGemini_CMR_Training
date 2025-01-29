class bird:   #parent class 1
    def fly(self):
        return "this bird can fly."
    
class mamal:  #parent class 2
    def walk(self):
        return "the mamal can walk."

class bat(bird,mamal):  #child class
    #pass
    def sees(self):
        return "bat sees"

b=bat()
print(b.fly()) #inherited from bird
print(b.walk())#inherited from mamal
print(b.sees())

