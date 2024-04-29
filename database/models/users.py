from datetime import datetime

from sqlalchemy import func
from database.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    join_date: Mapped[datetime] = mapped_column(server_default=func.now())
    active: Mapped[bool] = mapped_column(default=True)

    def __repr__(self):
        return f'User({self.user_id=}, {self.join_date=}, {self.active=}, {self.status=}'

