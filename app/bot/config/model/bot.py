from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    log_chat: int | None = None
