from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from dishka import Provider, Scope, provide
from redis.asyncio import Redis

from app.bot.config.model.bot import BotConfig


class BotProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_bot(self, config: BotConfig) -> Bot:
        return Bot(token=config.token, default=DefaultBotProperties(ParseMode.HTML))

    @provide
    async def get_storage(self, redis: Redis) -> RedisStorage:
        return RedisStorage(
            redis=redis,
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )

    @provide
    async def get_dp(self, storage: RedisStorage) -> Dispatcher:
        return Dispatcher(storage=storage)
