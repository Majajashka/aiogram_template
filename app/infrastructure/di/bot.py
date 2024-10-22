from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dishka import Provider, Scope, provide

from app.bot.config.model.bot import BotConfig


class BotProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_bot(self, config: BotConfig) -> Bot:
        return Bot(token=config.token, default=DefaultBotProperties(ParseMode.HTML))
