from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    pm = ProductManager()

    # adăugăm produse de test
    pm.add_product(Product("Tricou", 49.90, 10))
    pm.add_product(Product("Pantaloni", 129.00, 5))
    pm.add_product(Product("Șapcă", 39.50, 20))
    pm.add_product(Product("Geacă", 299.99, 3))
    pm.add_product(Product("Șosete", 9.99, 50))

    print("Produse disponibile:")
    pm.list_products()

    print(f"\nValoarea totală a inventarului: {pm.total_value():.2f} RON")

if __name__ == "__main__":
    main()
    cart = Cart()
    if len(pm.products) >= 3:
        choices = random.sample(pm.products, 3)
    else:
        choices = pm.products

    for prod in choices:
        cart.add_product(prod, qty=1)

    print("\nConținut coș:")
    cart.display_cart()
