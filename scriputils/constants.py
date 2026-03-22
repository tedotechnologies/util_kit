"""scriputils/constants.py

Logging level constants and helpers.
"""
import logging


def get_mapping() -> dict[str, int]:
    """Return a mapping of logging level names to their numeric values.

    Uses :func:`logging.getLevelNamesMapping` when available (Python 3.11+),
    falling back to a hardcoded mapping for older interpreters.

    :returns: Dictionary mapping level name strings to integer values.
    """
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
