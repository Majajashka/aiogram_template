import logging


def setup_logging(level: int = 10):
    logging.basicConfig(
        level=level,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
