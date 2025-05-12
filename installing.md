# Dependency Management

Installing 3rd-party packages from PyPI.

## Miki's Method
YMMV :)

- Create a virtual environment per project
    $ python -m venv .venv
    (don't forget to add .venv to .gitignore)
- **Make sure your IDE and terminal uses the Python from the virtual environment**
    - Terminal:
        - $ which python
    - IDE:
        - import sys
        - print(sys.executable)
- Write your requirements in a file (requirements.txt)
    - Add it to git
- $ ./.venv/bin/python -m pip install -r requirements.txt
- Optionally have development requirements (e.g. testing)
    - requirements-dev.txt
    - $ ./.venv/bin/python -m pip install -r requirements-dev.txt


On colab run:

    %pip install requests


## Risks of using 3rd-party packages

- Security
    - Ignorance
    - Bad actors
- Bugs
- Version (backward compatibility)
    - e.g. version 2.2 changed a method name from version 2.1
- Deleted code
- Legal (license)


## Limitation

Python can have only a single version of a package installed.
Meaning you can't have both pandas 2.1 & 2.2 in the same project.

## Solution: Virtual Environment

Each project gets their own Python.
