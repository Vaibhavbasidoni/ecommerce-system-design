class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def get_details(self) -> dict:
        return {"id": self.id, "name": self.name, "price": self.price}
