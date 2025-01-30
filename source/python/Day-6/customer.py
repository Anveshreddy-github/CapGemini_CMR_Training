class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def get_customer_info(self):
        return {"Customer ID": self.customer_id, "Name": self.name, "Email": self.email}

class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_order_details(self):
        return {"Order ID": self.order_id, "Items": [item.get_item_details() for item in self.items]}


class OrderItem(Order):
    def __init__(self, order_id, item_name, quantity, price):
        super().__init__(order_id)
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def get_item_details(self):
        return {"Item": self.item_name, "Quantity": self.quantity, "Price": self.price}

class CustomerOrder(Customer, Order):
    def __init__(self, customer_id, name, email, order_id):
        Customer.__init__(self, customer_id, name, email)
        Order.__init__(self, order_id)

    def get_full_order_details(self):
        details = self.get_customer_info()
        details.update(self.get_order_details())
        return details

# Create a transaction dictionary     
transaction = {}

# Dynamic User Input
customer_id = input("Enter Customer ID: ")
name = input("Enter Customer Name: ")
email = input("Enter Customer Email: ")
order_id = input("Enter Order ID: ")

# Create Customer Order Object
customer_order = CustomerOrder(customer_id, name, email, order_id)

while True:
    item_name = input("Enter Item Name (or type 'exit' to stop): ")
    if item_name.lower() == 'exit':
        break

    # Validate quantity input
    while True:
        try:
            quantity = int(input("Enter Quantity (must be a number): "))
            if quantity < 1:
                print("Quantity must be at least 1. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Validate price input
    while True:
        try:
            price = float(input("Enter Price (must be a number): "))
            if price < 0:
                print("Price cannot be negative. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Create OrderItem and add to customer_order
    item = OrderItem(order_id, item_name, quantity, price)
    customer_order.add_item(item)

# Store transaction in dictionary
transaction[customer_order.order_id] = customer_order.get_full_order_details()

# Print the Transaction
print("\nFinal Transaction Details:")
print(transaction)