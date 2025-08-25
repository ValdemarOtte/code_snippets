### Imports
# Standard library
import os

# Third-party libraries

# Local files


def clear() -> None:
    """
    Clear the terminal.
    """
    os.system("cls")


def run_command_in_terminal(command: str) -> None:
    """
    Run a command in the terminal.

    :param str command: The command which will be run in the terminal.
    """
    os.system(command)
