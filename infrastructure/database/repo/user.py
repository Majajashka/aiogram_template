from sqlalchemy.dialects.postgresql import insert

from .base import BaseRepo
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from core.dto.user import User
from infrastructure.database.models.users import UserOrm


class UserRepo(BaseRepo[UserOrm]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=UserOrm, session=session)

    async def get_by_id(self, id: int) -> User:
        return (await self._get_by_id(id)).to_dto()

    async def create_user(self, user: User) -> User:
        saved_user = await self.session.execute(
            insert(UserOrm)
            .values(
                id=user.id,
            )
            .returning(UserOrm)
        )
        return saved_user.scalar_one().to_dto()

    async def get_users_by_status(self, status: bool = True) -> int:
        users = await self.session.execute(select(func.count()).where(self.model.active == status))
        count = users.scalars().one()
        return count
