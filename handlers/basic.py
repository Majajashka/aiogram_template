from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

basic_router = Router()


@basic_router.message(CommandStart())
async def start(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.start(name=message.from_user.first_name))
