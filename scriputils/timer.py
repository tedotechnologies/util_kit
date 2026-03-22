"""scriputils/timer.py

Decorator for tracking function execution time.
"""
import functools
import logging
import time
from collections.abc import Callable
from typing import Any, TypeVar

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


def track(func: F) -> F:
    """Log the execution time of the decorated function.

    :param func: Function to wrap.
    :returns: Wrapped function that logs elapsed time at INFO level.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        func_result = func(*args, **kwargs)
        logger.info(f"{func.__module__}.{func.__name__} :: {time.time() - start:.2f}s")
        return func_result

    return wrapper  # type: ignore[return-value]
