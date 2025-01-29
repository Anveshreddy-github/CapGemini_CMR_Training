class destructor:
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print(f"object {self.name} is destroyed")
p=destructor("abj")
del p

