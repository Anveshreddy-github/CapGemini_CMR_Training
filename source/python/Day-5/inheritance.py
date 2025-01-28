class Parent:
    def __init__(self):
        self.BigNose="7CM"

    def display_parent(self):
        print("this is parent class")

class Child(Parent):
    def display_child(self):
        print("this is child class")

    def __init__(self):
        super().__init__()

    def BG(self):
        BigNose="9cm"
        print(BigNose)

q=Child()
q.display_child()
q.display_parent()
print(q.BigNose)
q.BG()


