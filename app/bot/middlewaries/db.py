import logging
from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery, Message

from app.core.service.user import get_or_create_user
from app.infrastructure.database.holder import HolderRepo

logger = logging.getLogger(__name__)


class DbSessionMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        async with data['dishka_container']() as di:
            holder = await di.get(HolderRepo)
            if isinstance(event, (Message, CallbackQuery)):
                data['user'] = await get_or_create_user(user_id=event.from_user.id, user_repo=holder.user_repo)
            try:
                await handler(event, data)
                await holder.session.commit()
            except Exception:
                await holder.session.rollback()
                raise
