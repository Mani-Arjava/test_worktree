from src.models.order import Order


class OrderService:
    def get_order(self, order_id: int) -> Order:
        raise NotImplementedError

    def create_order(self, user_id: int, product_id: int, quantity: int) -> Order:
        raise NotImplementedError
