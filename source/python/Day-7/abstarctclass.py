from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    def show(self):
        print("concrete method")#method implemented in abstart class is called concrete method 

class son(Father):
    def disp(self):
        print("son is implementing the abstract method")

class Daugther(Father):
    def disp(self):
        print("daugther is implementing the abstract method")

def main():
    s=son()
    s.disp()
    s.show()

    d=Daugther()
    d.disp()
    d.show()
main()

