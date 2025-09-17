### Imports
# Standard library
from pathlib import Path

# Third-party libraries

# Local files


def read_txt(path: Path, encoding: str = "UTF-8") -> list[str]:
    """
    Read txt-file and return lines.

    :param Path path: Path to txt-file.
    :param str encoding: Encoding for the txt-file. Default is `UTF-8`.
    :return list[str]: A list of strings with the content of the file.
    """
    with open(path, "r", encoding=encoding) as file:
        return [line.rstrip() for line in file]


def write_lines_to_txt(path: Path, lines: list[str], encoding: str = "UTF-8", mode: str = "w") -> None:
    """
    Write to a txt-file line by line.

    Default mode is `w` (write). Set mode to `a` for append to end for the txt-file.

    :param Path path: Path to txt-file.
    :param list[str] lines: List of strings, which will be writed to the txt-file.
    :param str encoding: Encoding for the txt-file. Default is `UTF-8`.
    :param str mode: Mode for file. Default is `w`.
    """
    with open(path, mode=mode, encoding=encoding) as file:
        for line in lines:
            file.write(f"{line}\n")
