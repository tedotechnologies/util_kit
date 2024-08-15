import logging
import time

logger = logging.getLogger(__name__)


def track(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_result = func(*args, **kwargs)
        logger.info(f"{func.__module__}.{func.__name__} :: {time.time() - start:.2f}s")
        return func_result

    return wrapper
