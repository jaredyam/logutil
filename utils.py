from pathlib import Path
from datetime import datetime

import __main__

try:
    EXEC_FILE = Path(__main__.__file__).stem
except AttributeError as e:
    EXEC_FILE = input('[Prompt/Notebook] Please assign a name to the current '
                      'file you are running : ')

EXEC_DATE = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')


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
