from aiogram import Router

from .basic import basic_router


def get_routers() -> list[Router]:
    return [
        basic_router
    ]
