from dishka import Provider

from .config import ConfigProvider
from .database import DatabaseProvider, RepoProvider


def get_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DatabaseProvider(),
        RepoProvider()
    ]
