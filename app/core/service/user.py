import logging

from sqlalchemy.exc import NoResultFound

from app.core.dto.user import User, UserActivity
from app.infrastructure.database.repo.user import UserRepo

logger = logging.getLogger(__name__)


async def get_or_create_user(user_id: int, user_repo: UserRepo) -> User:
    try:
        user = await user_repo.get_by_id(user_id)
    except NoResultFound:
        user = await user_repo.create_user(User(tg_id=user_id))
        logging.info('New user created %s', user)
    return user


async def get_users_count_by_status(repo: UserRepo) -> UserActivity:
    active = await repo.get_users_count_by_status(status=True)
    inactive = await repo.get_users_count_by_status(status=False)
    return UserActivity(active=active, inactive=inactive)
