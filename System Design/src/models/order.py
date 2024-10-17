from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

from .product import Product

class Order:
    def __init__(self, id: int, user: User):
        self.id = id
        self.user = user
        self.products: List[Product] = []
        self.total_amount = 0.0
        self.status = "pending"

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        self.total_amount += product.price

    def remove_product(self, product: Product) -> None:
        if product in self.products:
            self.products.remove(product)
            self.total_amount -= product.price

    def update_status(self, new_status: str) -> None:
        self.status = new_status

    def get_order_details(self) -> dict:
        return {
            "id": self.id,
            "user": self.user.name,
            "products": [p.get_details() for p in self.products],
            "total_amount": self.total_amount,
            "status": self.status
        }
