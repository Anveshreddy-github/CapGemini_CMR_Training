class customer:
    def __init__(self,c_id,name,phone,email,address):
        self.c_id=c_id
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address


class orders:
    def __init__(self,order_id,order_data):
        self.order_id=order_id
        self.order_data=order_data

class customerOrder(customer,orders):
    def __init__(self, c_id, order_id,order_data ):
        super().__init__(c_id,order_id,order_data)

        