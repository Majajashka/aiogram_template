import asyncio
import logging

from dishka.integrations.aiogram import setup_dishka as setup_aiogram_dishka

from aiogram import Bot, Dispatcher

from app.bot.factory import setup_di
from app.bot.keyboards.set_menu import set_main_menu
from app.bot.setup import setup_logging

logger = logging.getLogger(__name__)


async def main() -> None:
    setup_logging()
    logger.info('Starting bot...')

    logger.info('Setuping IoC...')
    di = setup_di()
    bot = await di.get(Bot)
    dp = await di.get(Dispatcher)
    setup_aiogram_dishka(container=di, router=dp, auto_inject=True)

    logger.info('Setting up menu...')
    await set_main_menu(bot)
    logger.info('Starting polling...')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
