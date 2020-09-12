import sys
from datetime import datetime
import logging
from pathlib import Path


class ColorfulFormatter(logging.Formatter):

    """
    A helper class used to change `logging.Formatter` default behavior
    with overriding the format method.
    We can get the concrete log information with `record`, e.g record.levelno.
    """

    def format(self, record):
        RESET_COLOR = '\033[39m'
        ASCTIME_COLOR = "\033[96m"
        WARNING_COLOR = "\033[33m"
        ERROR_COLOR = "\033[35m"
        CRITICAL_COLOR = "\033[31m"
        MSG_COLOR = '\033[39m'

        if record.levelno == logging.WARNING:
            MSG_COLOR = WARNING_COLOR
        if record.levelno == logging.ERROR:
            MSG_COLOR = ERROR_COLOR
        if record.levelno == logging.CRITICAL:
            MSG_COLOR = CRITICAL_COLOR

        return logging.Formatter(f'{ASCTIME_COLOR}%(asctime)s{RESET_COLOR}'
                                 f' - {record.levelname:<8} - '
                                 f'%(filename)s : %(module)s : %(lineno)d'
                                 f' : %(funcName)s - '
                                 f'{MSG_COLOR}%(message)s{RESET_COLOR}',
                                 "%Y-%m-%d-%H:%M:%S").format(record)


def create_logger(level='DEBUG',
                  console=True,
                  filename=None,
                  save=False):
    """Create a logger for the current module.

    Usage
    -----
    Console case  : logger = create_logger()
    Notebook case : logger = create_logger(notebook=True, filename=filename)

    Parameters
    ----------
    level    : str [default: debug]
        Level to filter messages. Both lower and upper cases are accepted.
        LEVELS available: ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    console  : boolen
        Set it to False if you don't want to print logs to the console.

    filename : str
        Need to be assigned if you are using prompt or notebook.

    save     : boolen
        Set to True if you want to save the log.
        Default save path: ./log/filename/%Y%m%d_%H%M%S.log

        exec_file.py
        log
        └── exec_file
            └── time_stamp.log

    """

    LOG_PATH = Path('./log')

    if filename is None:
        try:
            import __main__
            filename = Path(__main__.__file__).stem
        except AttributeError as e:
            print(e, 'Set a value to the `filename` argument'
                  'if you are using prompt or notebook.', sep='\n')
            sys.exit(1)

    logger = logging.getLogger(filename)
    logger.setLevel(getattr(logging, level.upper()))

    if not logger.handlers:
        if save:
            formatter = logging.Formatter('%(asctime)s'
                                          ' - %(levelname)s - '
                                          '%(filename)s : %(module)s : '
                                          '%(lineno)d : %(funcName)s - '
                                          '%(message)s',
                                          "%Y-%m-%d-%H:%M:%S")
            date = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
            log_file_path = LOG_PATH / filename
            log_file_path.mkdir(exist_ok=True, parents=True)

            file_handler = logging.FileHandler(log_file_path / f'{date}.log')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        if console:
            formatter = ColorfulFormatter()
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)

    logger.propagate = False

    return logger
