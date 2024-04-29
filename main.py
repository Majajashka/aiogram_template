import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import Redis, RedisStorage
from fluentogram import TranslatorHub

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from handlers import basic
from language.translator import translator_hub
from middlewaries.db import DbSessionMiddleware

from config import load_config, Config
from middlewaries.translator import TranslatorMD

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')

    config: Config = load_config('.env')
    t_hub: TranslatorHub = translator_hub()

    redis = Redis(host='localhost')
    storage = RedisStorage(redis=redis)

    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)

    async_engine = create_async_engine(config.db.db_url)
    sessionmaker = async_sessionmaker(async_engine)

    dp.workflow_data.update({'redis': redis, "_translator_hub": t_hub})

    logger.info('Подключаем роутеры')
    dp.include_routers(basic.basic_router)

    logger.info('Подключаем миддлвари')
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    dp.update.middleware(TranslatorMD())

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
