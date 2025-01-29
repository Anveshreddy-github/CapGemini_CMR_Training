class cat:
    def sound(self):
        print("meom")
    def name(self):
        print("rose")
    
class dog:
    def sound(self):
        print("bark")

for animal in (cat(),dog()):
    animal.sound()

d=dog()
d.sound()
c=cat()
c.name()