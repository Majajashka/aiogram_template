from sqlalchemy.exc import NoResultFound

from infrastructure.database.repo.user import UserRepo
from core.dto.user import User, UserActivity


async def create_user(user: User, repo: UserRepo) -> User:
    user = await repo.create_user(user)
    await repo.commit()
    return user


async def get_user_by_id(id: int, repo: UserRepo):
    try:
        user = await repo.get_by_id(id)
    except NoResultFound:
        user = None
    return user


async def get_all_user_by_status(repo: UserRepo) -> UserActivity:
    active = await repo.get_users_by_status(status=True)
    inactive = await repo.get_users_by_status(status=False)
    return UserActivity(active=active, inactive=inactive)
