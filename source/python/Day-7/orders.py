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
