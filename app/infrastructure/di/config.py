from dishka import Provider, Scope, provide

from app.bot.config.model.bot import BotConfig
from app.bot.config.parser.main import parse_bot_config
from app.infrastructure.database.configs.models import DatabaseConfig, RedisConfig
from app.infrastructure.database.configs.parsers import load_database_config, load_redis_config


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    async def provide_bot_config(self) -> BotConfig:
        return parse_bot_config()

    @provide
    def get_database_config(self) -> DatabaseConfig:
        return load_database_config()

    @provide
    def get_redis_config(self) -> RedisConfig:
        return load_redis_config()
