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
    def find_product_index(self, name: str):
        for i, p in enumerate(self.products):
            if p.name == name:
                return i
        return None

    def remove_product_by_name(self, name: str):
        idx = self.find_product_index(name)
        if idx is None:
            print(f"Produsul '{name}' nu a fost găsit.")
            return False
        removed = self.products.pop(idx)
        print(f"Am eliminat produsul: {removed.display()}")
        return True
