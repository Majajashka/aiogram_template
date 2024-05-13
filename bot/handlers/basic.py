import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from infrastructure.database.holder import HolderRepo
from core.service.user import create_user, get_user_by_id
from core.dto.user import User

basic_router = Router()
logger = logging.getLogger(__name__)


@basic_router.message(CommandStart())
async def start(message: Message, i18n: TranslatorRunner, repo: HolderRepo):
    await message.answer(i18n.start(name=message.from_user.first_name))

    user = await get_user_by_id(message.from_user.id, repo.users)
    if not user:
        user_dto = User(
            id=message.from_user.id
        )
        user = await create_user(user_dto, repo.users)
        logger.info(
            f'New user created: {message.from_user.first_name} - User ID: {user.id}, Active: {user.active},'
            f' Language: {user.language}, Created at: {user.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
        )
