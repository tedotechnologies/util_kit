"""scriputils/utils.py

Utility functions for configuration loading, logging setup, and CLI argument parsing.
"""
from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any

import yaml

from scriputils.constants import get_mapping


def get_config(path: Path) -> dict[str, Any]:
    """Load a YAML configuration file.

    :param path: Path to the YAML configuration file.
    :returns: Parsed configuration as a dictionary.
    """
    with open(path, encoding="utf-8") as conf_file:
        exp_config = yaml.load(conf_file, Loader=yaml.SafeLoader)
    return exp_config


def get_logger(
        logger_name: str | None = None,
        path: Path | None = None,
        level: int = logging.DEBUG,
        add_stdout: bool = False,
) -> logging.Logger:
    """Configure and return a logger with a file handler.

    :param logger_name: Name of the logger. Defaults to ``"logs"``.
    :param path: Directory for log files. Defaults to ``./logs``.
    :param level: Logging level.
    :param add_stdout: If ``True``, also log to stdout.
    :returns: Configured :class:`logging.Logger` instance.
    """
    logger_name = "logs" if logger_name is None else logger_name
    path_to_logs = Path("logs") if path is None else Path(path)
    path_to_logs.mkdir(parents=True, exist_ok=True)
    filename = path_to_logs / f"{logger_name}.log"
    print(f'Log file path: {filename.absolute()}')

    # create formatter with level name, module, line number, time and message
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
    )

    # create logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Prevent adding handlers multiple times
    if not any(isinstance(handler, logging.FileHandler) and handler.baseFilename == str(filename) for handler in root_logger.handlers):
        # create file handler
        file_handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    if add_stdout:
        # create stdout handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    return logger


def get_kwargs(default_config_path: Path) -> argparse.ArgumentParser:
    """Build an argument parser with ``--config_path`` and ``--logger_level`` options.

    :param default_config_path: Default path to the YAML configuration file.
    :returns: Configured :class:`argparse.ArgumentParser`.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--config_path', metavar='</path/to/config>',
        type=lambda p: Path(p),
        help=(f"pass path to config.yaml\nUse {default_config_path}."
              f"example to create new config.yaml file"),
        default=default_config_path
    )
    parser.add_argument(
        '-l', '--logger_level', metavar='<logger_level>',
        type=int,
        help=yaml.dump(get_mapping()),
        default=logging.INFO
    )
    return parser
