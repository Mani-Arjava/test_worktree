from src.models.user import User


class UserService:
    def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    def create_user(self, name: str, email: str) -> User:
        raise NotImplementedError
