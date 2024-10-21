from dishka import AsyncContainer, make_async_container

from app.infrastructure.di import get_providers


def setup_di() -> AsyncContainer:
    container = make_async_container(*get_providers())
    return container
