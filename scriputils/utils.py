# scriputils/utils.py
import argparse
import logging
import sys
from pathlib import Path
from typing import Dict, Any, Optional
import yaml


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
        "%(levelname)-8s [%(asctime)s] %(name)s:%(lineno)d: %(message)s"
    )

    # create file handler
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # create logger
    logger = logging.getLogger(logger_name)
    logger.addHandler(file_handler)
    logger.setLevel(level)
    if add_stdout:
        # create stdout handler
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)
    logging.basicConfig(level=level, handlers=logger.handlers)
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
        help=yaml.dump(logging.getLevelNamesMapping()),
        default=logging.INFO
    )
    return parser
