from aiogram import Dispatcher

from .db import DbSessionMiddleware
from .translator import TranslatorMD


def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware(TranslatorMD())
    dp.update.middleware(DbSessionMiddleware())
