from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/admin_list',
                   description='Список админов')
    ]

    await bot.delete_my_commands()
    return await bot.set_my_commands(main_menu_commands)
