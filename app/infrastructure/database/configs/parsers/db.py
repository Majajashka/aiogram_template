import os

from app.infrastructure.database.configs.models import DatabaseConfig, RedisConfig


def load_database_config() -> DatabaseConfig:
    return DatabaseConfig(
        login=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        port=int(os.getenv('POSTGRES_PORT'))
    )


def load_redis_config() -> RedisConfig:
    return RedisConfig(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT')),
        database=int(os.getenv('REDIS_DATABASE', 0))
    )
