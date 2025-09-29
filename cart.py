from product import Product
from typing import List, Tuple

class Cart:
    def __init__(self):
        self.cart_items: List[Tuple[Product, int]] = []

    def add_product(self, product: Product, qty: int = 1) -> None:
        self.cart_items.append((product, qty))
        print(f"Added to cart: {product.name} x{qty}")

    def total_price(self) -> float:
        return sum(p.price * q for p, q in self.cart_items)

    def display_cart(self) -> None:
        if not self.cart_items:
            print("Coșul este gol.")
            return
        for p, q in self.cart_items:
            print(f"{p.name} x{q} -> {p.price * q:.2f} RON")
        print(f"Total de plată: {self.total_price():.2f} RON")
