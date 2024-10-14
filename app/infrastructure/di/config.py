from dishka import Provider, Scope, provide

from app.bot.config.model.bot import BotConfig
from app.bot.config.parser.main import parse_bot_config


class ConfigProvider(Provider):
    scope = Scope.APP

    @provide
    async def provide_bot_config(self) -> BotConfig:
        return parse_bot_config()
