import os

from app.bot.config.model.bot import BotConfig


def parse_bot_config():
    return BotConfig(
        token=os.getenv('BOT_TOKEN'),
    )