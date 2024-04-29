from .base import BaseRepo


class UsersRepo(BaseRepo):
    def get_user(self, id: int):
        ...
