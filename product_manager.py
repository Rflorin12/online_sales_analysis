from product import Product
from typing import List

class ProductManager:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def list_products(self) -> None:
        if not self.products:
            print("Nu există produse.")
            return
        for p in self.products:
            print(p.display())

    def total_value(self) -> float:
        return sum(p.price * p.quantity for p in self.products)
