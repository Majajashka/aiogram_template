import logging

from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from dishka import AsyncContainer, make_async_container, Provider, Scope, provide
from fluentogram import TranslatorHub
from redis.asyncio import Redis

from app.bot.handlers import get_routers
from app.bot.language.translator import setup_translator_hub
from app.bot.middlewaries import setup_middlewares
from app.infrastructure.di import get_providers

logger = logging.getLogger(__name__)


def setup_di() -> AsyncContainer:
    container = make_async_container(*get_providers(), DpProvider())
    return container


class DpProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_dp(self, storage: RedisStorage) -> Dispatcher:
        dp = Dispatcher(storage=storage)
        logger.info('Including routers...')
        dp.include_routers(*get_routers())
        logger.info('Setting up middlewares...')
        setup_middlewares(dp)
        return dp

    @provide
    async def get_storage(self, redis: Redis) -> RedisStorage:
        return RedisStorage(
            redis=redis,
            key_builder=DefaultKeyBuilder(with_bot_id=True, with_destiny=True),
        )

    @provide
    async def get_i18n(self) -> TranslatorHub:
        return setup_translator_hub()
