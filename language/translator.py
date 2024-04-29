from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def translator_hub() -> TranslatorHub:
    t_hub: TranslatorHub = TranslatorHub(
        locales_map={
            'ru': ('ru',)
        },
        translators=[
            FluentTranslator(
                locale='ru',
                translator=FluentBundle.from_files(
                    'ru-RU', filenames=["language/locales/ru.ftl"]
                )
            )
        ],
        root_locale='ru'
    )
    return t_hub
