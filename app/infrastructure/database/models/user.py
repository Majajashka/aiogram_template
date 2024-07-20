from sqlalchemy import BigInteger, true, false
from sqlalchemy.orm import Mapped, mapped_column

from app.core.dto.user import User
from app.infrastructure.database.models.base import Base, TimestampMixin


class UserOrm(Base, TimestampMixin):
    __tablename__ = 'users'

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    language: Mapped[str] = mapped_column(default='ru')
    is_banned: Mapped[bool] = mapped_column(server_default=false())
    is_active: Mapped[bool] = mapped_column(server_default=true())

    def __repr__(self):
        return (f'User(tg_id={self.tg_id}, is_active={self.is_active},'
                f' language={self.language}, is_banned={self.is_banned}'
                f' created_at={self.created_at},'
                f' updated_at={self.updated_at})')

    def to_dto(self) -> User:
        return User(
            tg_id=self.tg_id,
            is_active=self.is_active,
            is_banned=self.is_banned,
            language=self.language,
            created_at=self.created_at
        )
