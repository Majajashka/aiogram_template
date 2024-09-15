from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.repo.user import UserRepo


class HolderRepo:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.users = UserRepo(session=self.session)
