import sys

print(sys)  # built-in
print(sys.version_info)

import uuid

print(uuid)  # uuid.py

import math

print(math)  # math.cpython-313-x86_64-linux-gnu.so

import json

print(json)  # json/__init__.py

# __init__ is called "dunder init"

# Python can import
# - files ending with .py
# - directory containing __init__.py
# - .so
# - built-in (e.g. sys)
# Python will search sys.path to import
# You can prepend directories to sys.path using the PYTHONPATH
# environment variable
# Code smell: changing sys.path

# Python looks in sys.path for modules to import
from pprint import pprint

pprint(sys.path)

from pathlib import Path


def simulate_import(module_name):
    for dir_name in sys.path:
        py_file = Path(f'{dir_name}/{module_name}.py')
        if py_file.is_file():
            print(f'importing {py_file}')
            return

        init_file = Path(f'{dir_name}/{module_name}/__init__.py')
        if init_file.is_file():
            print(f'importing {init_file}')
            return

    raise ImportError(f'module {module_name} not found')


simulate_import('json')
simulate_import('uuid')

# Naming
import json

# need to prefix json. when accessing
data = json.dumps({'login': 'elliot', 'path': '/etc/passwd'})
print(data)

from urllib.request import urlopen

# no need for prefix
with urlopen('https://google.com'):
    pass

# both ways (json, urlopen) load the whole module to memory

# When you do:
#   from json import dumps
#   ...  # 200 lines of code
#   data = dumps({'login': 'elliot', 'path': '/etc/passwd'})
# It's not clear where "dumps" comes from or what it does
# Seeing "json.dumps" is clear
# OTOH: urlopen is self explaining name
# Rule of thumb:
#     Use the shortest import form that is still readable

# You also rename imports
import math as m

print(m.sin(90))
print(m.sin(m.radians(90)))

from math import sqrt as square_root

print(square_root(2))

# Most common renames are in scientific stack:
# import pandas as pd
# import numpy as np

# NEVER DO IMPORT *
e = 70

from math import *

print(f'{e=}')  # 2.718...
