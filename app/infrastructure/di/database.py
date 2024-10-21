from typing import AsyncIterable

from dishka import provide, Scope, Provider
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession
from app.infrastructure.database.factory import create_async_engine, create_sessionmaker

from app.infrastructure.database.configs.models import DatabaseConfig, RedisConfig
from app.infrastructure.database.holder import HolderRepo


class DatabaseProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_async_engine(self, db_config: DatabaseConfig) -> AsyncIterable[AsyncEngine]:
        engine = create_async_engine(db_config, pool_size=100, max_overflow=15,  pool_timeout=300)
        yield engine
        await engine.dispose(True)

    @provide
    def get_sessionmaker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return create_sessionmaker(engine)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, sessionmaker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        session = sessionmaker()
        try:
            yield session
        finally:
            await session.close()

    @provide
    async def get_redis(self, config: RedisConfig) -> Redis:
        return Redis(
            host=config.host,
            port=config.port,
            db=config.database
        )


class RepoProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_holder_repo(self, session: AsyncSession) -> AsyncIterable[HolderRepo]:
        yield HolderRepo(session)
