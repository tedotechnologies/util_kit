import logging


def get_mapping() -> dict[str, int]:
    try:
        return logging.getLevelNamesMapping()
    except AttributeError:
        return {
            "CRITICAL": 50,
            "ERROR": 40,
            "WARNING": 30,
            "INFO": 20,
            "DEBUG": 10,
            "NOTSET": 0,
        }
