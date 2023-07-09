from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        product = [p for p in self.products if p.name == product_name]
        if product:
            return product[0]

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = [f"{p.name}: {p.quantity}" for p in self.products]

        return "\n".join(result)





