from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine
from config import load_config, Config

config = load_config()


def create_async_eng(config: Config):
    return create_async_engine(
        url=config.db.db_url(),
    )


def create_sync_engine(config: Config):
    return create_engine(
        url=config.db.db_url(),
    )

def async_session(config: Config):
    return async_sessionmaker(create_async_engine(config))
