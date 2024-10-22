from pathlib import Path

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def get_ftl_files(locale: str) -> list[Path]:
    dir_path = Path(f'app/bot/language/locales/{locale}/')

    ftl_files = [file for file in dir_path.glob('*.ftl') if file.is_file()]

    return ftl_files


def setup_translator_hub() -> TranslatorHub:
    t_hub: TranslatorHub = TranslatorHub(
        locales_map={
            'ru': ('ru',)
        },
        translators=[
            FluentTranslator(
                locale='ru',
                translator=FluentBundle.from_files(
                    'ru-RU', filenames=get_ftl_files(locale='ru'),
                    use_isolating=False
                )
            )
        ],
        root_locale='ru'
    )
    return t_hub
