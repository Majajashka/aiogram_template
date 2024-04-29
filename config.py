from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных
    db_port: str  # Порт базы данных

    @property
    def db_url(self):
        return f"postgresql+psycopg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}"f"/{self.database}"


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список айди админов


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD'),
            db_port=env('DB_PORT')
        )
    )


if __name__ == '__main__':
    config = load_config()
    print('BOT_TOKEN:', config.tg_bot.token)
    print('ADMIN_IDS:', config.tg_bot.admin_ids)
    print()
    print('DATABASE:', config.db.database)
    print('DB_PORT', config.db.db_port)
    print('DB_HOST:', config.db.db_host)
    print('DB_USER:', config.db.db_user)
    print('DB_PASSWORD:', config.db.db_password)
    print('DB_URL:', config.db.db_url)
