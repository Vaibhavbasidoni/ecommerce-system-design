from typing import List, Optional
from models.user import User
from models.product import Product
from models.order import Order
from models.payment import Payment

class ECommerceSystem:
    def __init__(self):
        self.users: List[User] = []
        self.products: List[Product] = []
        self.orders: List[Order] = []
        self.payments: List[Payment] = []
        self.next_user_id = 1
        self.next_product_id = 1
        self.next_order_id = 1
        self.next_payment_id = 1

    def register_user(self, name: str, email: str) -> User:
        user = User(self.next_user_id, name, email)
        self.next_user_id += 1
        self.users.append(user)
        return user

    def add_product(self, name: str, price: float) -> Product:
        product = Product(self.next_product_id, name, price)
        self.next_product_id += 1
        self.products.append(product)
        return product

    def create_order(self, user_id: int) -> Order:
        user = next((u for u in self.users if u.id == user_id), None)
        if user:
            order = Order(self.next_order_id, user)
            self.next_order_id += 1
            self.orders.append(order)
            return order
        return None

    def process_payment(self, order_id: int, payment_method: str) -> bool:
        order = next((o for o in self.orders if o.id == order_id), None)
        if order:
            payment = Payment(self.next_payment_id, order, order.total_amount, payment_method)
            self.next_payment_id += 1
            self.payments.append(payment)
            return True
        return False

    def get_user_orders(self, user_id: int) -> List[Order]:
        user = next((u for u in self.users if u.id == user_id), None)
        if user:
            return user.view_orders()
        return []

    def update_order_status(self, order_id: int, new_status: str) -> None:
        order = next((o for o in self.orders if o.id == order_id), None)
        if order:
            order.update_status(new_status)

    # Helper methods
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        return next((order for order in self.orders if order.id == order_id), None)

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return next((product for product in self.products if product.id == product_id), None)

    def add_product_to_order(self, order_id: int, product_id: int) -> None:
        order = self.get_order_by_id(order_id)
        product = self.get_product_by_id(product_id)
        if order and product:
            print(f"Adding product {product.name} to order {order_id}")  # Debug print
            order.add_product(product)
            print(f"Order {order_id} now has {len(order.products)} products")  # Debug print
        else:
            raise ValueError(f"Order with id {order_id} or Product with id {product_id} not found")

    def remove_product_from_order(self, order_id: int, product_id: int) -> None:
        order = self.get_order_by_id(order_id)
        product = self.get_product_by_id(product_id)
        if order and product:
            order.remove_product(product)
        else:
            raise ValueError(f"Order with id {order_id} or Product with id {product_id} not found")
