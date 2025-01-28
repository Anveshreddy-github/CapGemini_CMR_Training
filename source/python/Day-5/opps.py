class car:
    def __init__ (self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"this car is : {self.brand} {self.model}")
car_obj=car("tata","nano")
car_obj.display()  
