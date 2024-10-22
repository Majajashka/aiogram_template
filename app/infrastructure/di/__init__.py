from dishka import Provider

from .bot import BotProvider
from .config import ConfigProvider
from .database import DatabaseProvider, RepoProvider


def get_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DatabaseProvider(),
        RepoProvider(),
        BotProvider()
    ]
