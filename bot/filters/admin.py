from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import Config


class IsAdmin(BaseFilter):

    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message, config: Config) -> bool:
        return message.from_user.id in config.tg_bot.admin_ids
