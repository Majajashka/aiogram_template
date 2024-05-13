import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
from typing import TypeVar, Generic

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from infrastructure.database.models.users import UserOrm
from infrastructure.database.models.base import Base

Model = TypeVar('Model', bound=Base, covariant=True, contravariant=False)

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())


class BaseRepo(Generic[Model]):
    """
    A class representing a base repository for handling database operations.

    Attributes:
        session (AsyncSession): The database session used by the repository.
        model (Model): The database table model.
    """

    def __init__(self, session: AsyncSession, model: type[Model]) -> None:
        self.session: AsyncSession = session
        self.model = model

    async def _get_by_id(self, id: int) -> UserOrm:
        r = await self.session.get(
            self.model,
            id,
        )
        if r is None:
            raise NoResultFound
        return r

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
