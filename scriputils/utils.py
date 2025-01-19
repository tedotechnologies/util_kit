# scriputils/utils.py
import argparse
import logging
import sys
from pathlib import Path
from typing import Dict, Any

import yaml

from scriputils.constants import get_mapping


def get_config(path: Path) -> Dict[str, Any]:
    r"""Get anything what was in yaml. Probably dict"""
    with open(str(path)) as conf_file:
        exp_config = yaml.load(conf_file, Loader=yaml.Loader)
    return exp_config


def get_logger(
        logger_name: str | None = None,
        path: Path | None = None,
        level: int = logging.DEBUG,
        add_stdout: bool = False
) -> logging.Logger:
    """
    Get logger with file handler
    Parameters
    ----------
    logger_name: str|None
        Name of logger
    path: Path|None
        Path to log file
    level: int
        Level of logger
    add_stdout: bool
        if true logger will print to stdout too
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
    r"""Kwargs parser for drill health and accident experiments launchers"""
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
