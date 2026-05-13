from src.models.product import Product


class ProductService:
    def get_product(self, product_id: int) -> Product:
        raise NotImplementedError

    def create_product(self, name: str, price: float) -> Product:
        raise NotImplementedError
