from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery, Message
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.core.service.user import get_or_create_user
from app.infrastructure.database.holder import HolderRepo


class DbSessionMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker):
        super().__init__()
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with self.session_pool() as session:
            holder = HolderRepo(session=session)
            data['repo'] = holder
            if isinstance(event, (Message, CallbackQuery)):
                data['user'] = await get_or_create_user(user_id=event.from_user.id, user_repo=holder.user_repo)
            await handler(event, data)
            await session.commit()
