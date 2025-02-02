class product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    
    def check_avalibility(self,quantity):
        if self.stock >= quantity:
            return "required quantity is available"
        else:
            return "required quntity is not available"

def main():
    name=input("enter the name of the product:")
    price=input("enter price :")
    stock=input("enter stock:")
    p=product(name,price,stock)
    required_quantity=input("enter required quantity:")
    print(p.check_avalibility(required_quantity))
main()

