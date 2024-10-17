from .order import Order

class Payment:
    def __init__(self, id: int, order: Order, amount: float, payment_method: str):
        self.id = id
        self.order = order
        self.amount = amount
        self.payment_method = payment_method
        self.status = "pending"

    def process_payment(self) -> bool:
        self.status = "completed"
        return True

    def get_payment_status(self) -> str:
        return self.status
