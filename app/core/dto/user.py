from datetime import datetime
from dataclasses import dataclass

from app.core.dto.base import Base


class User(Base):
    tg_id: int
    is_active: bool = None
    language: str = None
    is_banned: bool = None
    created_at: datetime = None


@dataclass
class UserActivity(Base):
    """Сount of active and inactive users"""
    active: int
    inactive: int
