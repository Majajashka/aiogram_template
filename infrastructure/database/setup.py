from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlalchemy import create_engine

from config import Config


def create_async_eng(config: Config):
    return create_async_engine(
        url=config.db.db_url,
    )


def create_sync_engine(config: Config):
    return create_engine(
        url=config.db.db_url,
    )


def async_session(engine: AsyncEngine):
    return async_sessionmaker(engine)
