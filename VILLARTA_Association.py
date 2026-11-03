class Customer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

class Order:
    def __init__(self, order_id: int, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        customer.orders.append(self)

alice = Customer("Alice")
order1 = Order(101, alice)
order2 = Order(102, alice)
print(f"Customer Profile: {alice.name}")
for o in alice.orders:
    print(f"Order ID: {o.order_id}")