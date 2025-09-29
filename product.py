class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)

    def display(self) -> str:
        return f"{self.name} - {self.price:.2f} RON - qty: {self.quantity}"

    def update_quantity(self, new_qty: int) -> None:
        self.quantity = int(new_qty)

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r}, {self.quantity!r})"
