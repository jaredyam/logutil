# 📦 Logutil

A collection of scripts used to create and analysis log files.

### Pre-defined default log path

```
...
exec_file.py
...
logs
└── exec_file
    └── time_stamp.log
```

### Usage

#### logger.py

```python
from src import create_logger

logger = create_logger()

...
```

#### lastlog.sh

You can just `source` it or add the `lastlog` function to your shell configure file (e.g. `~/.bashrc` or `~/.zshrc`).

```bash
# open the last log file with sublime
$ lastlog -c

# print out the specific level message to console
$ lastlog -a level=error
```
