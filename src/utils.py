import sys
from pathlib import Path
from datetime import datetime

import __main__


class Color:

    """A cluster of colors used to annotate messages in the terminal.

    """

    RESET = '\033[0m'
    GREEN = '\033[96m'
    ORANGE = '\033[33m'
    DARKRED = '\033[35m'
    DARKCYAN = '\033[36m'
    PURPLE = '\033[95m'
    RED = '\033[31m'


try:
    EXEC_FILE = Path(__main__.__file__).stem
    if EXEC_FILE == 'pytest':
        raise AttributeError
except AttributeError:
    if sys.argv and Path(sys.argv[0]).name != 'ipykernel_launcher.py':
        EXEC_FILE = Path(sys.argv[1]).resolve().stem
    else:
        EXEC_FILE = input(f"{Color.GREEN}[Notebook]{Color.RESET} "
                          "Can't recognize the name of the current notebook"
                          ", which could be a problem when you want to save"
                          " some outputs. "
                          "Please assign a name to the current file : ")

EXEC_DATE = f'{datetime.now():%Y-%m-%d-%H-%M-%S}'


def save_dir(category):
    """Generate a nested directory for saving the output.

    Parameters
    ----------
    category : Path
        Which category the output files belonging to.

    Returns
    -------
    Path
        The created directory path.
    """
    filedir = category / EXEC_FILE
    filedir.mkdir(exist_ok=True, parents=True)
    return filedir
