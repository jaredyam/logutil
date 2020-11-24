import logging
from pathlib import Path

from .utils import EXEC_FILE, EXEC_DATE, Color
from .utils import save_dir


def create_logger(level='DEBUG',
                  save=False,
                  console=True):
    """Create a logger with pre-defined configure.

    Parameters
    ----------
    level : str [default: debug]
        Level to filter messages. Both lower and upper cases are accepted.
        LEVELS available: ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    save : boolen
        Set to True if you want to save the log.
        Default save path: ./log/exec_file/%Y-%m-%d-%H-%M-%S.log

        exec_file.py
        log
        └── exec_file
            └── time_stamp.log
    console : boolen
        Set to False if you don't want to print out logs to the console.

    """

    LOG_PATH = Path('./logs')

    logger = logging.getLogger(EXEC_FILE)
    logger.setLevel(getattr(logging, level.upper()))

    if not logger.handlers:
        if save:
            formatter = logging.Formatter('%(asctime)s'
                                          ' - %(levelname)s - '
                                          '%(filename)s : %(module)s : '
                                          '%(lineno)d : %(funcName)s - '
                                          '%(message)s',
                                          "%Y-%m-%d-%H:%M:%S")
            log_file_path = save_dir(LOG_PATH) / f'{EXEC_DATE}.log'

            file_handler = logging.FileHandler(log_file_path)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        if console:
            formatter = ColorfulFormatter()
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

    logger.propagate = False

    return logger


class ColorfulFormatter(logging.Formatter):

    """
    A helper class used to change the default behavior of class
    `logging.Formatter` with overriding the format method.

    Note
    ----
    We can get the log level information with the attribute `levelno`.

    """

    def format(self, record):

        MSG_COLOR = Color.RESET

        if record.levelno == logging.WARNING:
            MSG_COLOR = Color.DARKRED
        if record.levelno == logging.ERROR:
            MSG_COLOR = Color.RED
        if record.levelno == logging.CRITICAL:
            MSG_COLOR = Color.ORANGE

        return logging.Formatter(f'{Color.GREEN}%(asctime)s{Color.RESET}'
                                 f' - {record.levelname:<8} - '
                                 f'%(filename)s : %(module)s : %(lineno)d'
                                 f' : %(funcName)s - '
                                 f'{MSG_COLOR}%(message)s{Color.RESET}',
                                 "%Y-%m-%d-%H:%M:%S").format(record)
