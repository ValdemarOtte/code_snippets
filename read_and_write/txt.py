### Imports
# Standard library
from pathlib import Path

# Third-party libraries

# Local files


def read_txt(path: Path, encoding: str = "UTF-8") -> list[str]:
    """
    Read txt-file and return lines.

    :param Path txt_path: Path to txt-file.
    :param str encoding: Encoding for the txt-file. Default is 'UTF-8'.
    :return list[str]: A list of strings with the content of the file.
    """
    with open(path, "r", encoding=encoding) as file:
        return [line.rstrip() for line in file]


def write_lines_to_txt(lines: list[str], path: Path, encoding: str = "UTF-8") -> None:
    """
    Write to a txt-file line by line.

    :param list[str] lines: List of strings, which will be writed to the txt-file.
    :param str encoding: Encoding for the txt-file. Default is 'UTF-8'.
    :param Path txt_path: Path to txt-file.
    """
    with open(path, "w", encoding=encoding) as file:
        for line in lines:
            file.write(f"{line}\n")


def append_lines_to_txt(lines: list[str], path: Path, encoding: str = "UTF-8") -> None:
    """
    Append lines to a txt-file.

    :param list[str] lines: List of strings, which will be appned to the txt-file.
    :param str encoding: Encoding for the txt-file. Default is 'UTF-8'.
    :param Path txt_path: Path to txt-file.
    """
    with open(path, "w", encoding=encoding) as file:
        for line in lines:
            file.write(f"{line}\n")