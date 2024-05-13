import enum

from sqlalchemy import BigInteger, true
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import Base, TimestampMixin
from core.dto.user import User


class UserOrm(Base, TimestampMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    active: Mapped[bool] = mapped_column(server_default=true())
    language: Mapped[str] = mapped_column(default='ru')

    def __repr__(self):
        return f'User(id={self.id}, active={self.active}, language={self.language}, created_at={self.created_at.strftime("%Y-%m-%d %H:%M:%S")}, updated_at={self.updated_at.strftime("%Y-%m-%d %H:%M:%S")})'

    def to_dto(self) -> User:
        return User(
            id=self.id,
            active=self.active,
            language=self.language,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


if __name__ == '__main__':
    from infrastructure.database.setup import create_sync_engine
    from config import load_config

    config = load_config()
    engine = create_sync_engine(config)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
