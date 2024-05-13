from datetime import datetime

from core.dto.base import Base


class User(Base):
    id: int
    active: bool = None
    language: str = None
    created_at: datetime = None
    updated_at: datetime = None


class UserActivity(Base):
    """count of active and inactive users"""
    active: int = None
    inactive: int = None
