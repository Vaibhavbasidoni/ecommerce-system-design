from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.orders: List['Order'] = []

    def create_order(self) -> 'Order':
        from .order import Order
        order = Order(len(self.orders) + 1, self)
        self.orders.append(order)
        return order

    def view_orders(self) -> List['Order']:
        return self.orders

    def manage_order(self, order_id: int) -> None:
        order = next((o for o in self.orders if o.id == order_id), None)
        if order:
            print(f"Managing order {order_id} for user {self.name}")
        else:
            print(f"Order with id {order_id} not found for user {self.name}")
