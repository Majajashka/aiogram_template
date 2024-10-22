from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from app.core.dto.base import Base


class User(Base):
    tg_id: int
    is_active: Optional[bool] = None
    language: Optional[str] = None
    is_banned: Optional[bool] = None
    created_at: Optional[datetime] = None


@dataclass
class UserActivity(Base):
    """Сount of active and inactive users"""
    active: int
    inactive: int
