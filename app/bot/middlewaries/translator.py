from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from fluentogram import TranslatorHub


class TranslatorMD(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        di = data['dishka_container']
        hub = await di.get(TranslatorHub)
        data['i18n'] = hub.get_translator_by_locale('ru')
        return await handler(event, data)
