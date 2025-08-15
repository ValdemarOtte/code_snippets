### Imports
# Standard library
from pathlib import Path

# Third-party libraries

# Local files


def read_txt(path: Path) -> list[str]:
    """
    Read txt-file and return lines.

    :param Path txt_path: Path to txt-file.
    :return list[str]: A list of strings with the content of the file.
    """
    with open(path, "r", encoding="UTF-8") as file:
        return [line.rstrip() for line in file]


def write_txt(lines: list[str], path: Path) -> None:
    """
    Write to a txt-file line by line.

    :param list[str] lines: List of strings, which will be writed to the txt-file.
    :param Path txt_path: Path to txt-file.
    """
    with open(path, "w", encoding="UTF-8") as file:
        for line in lines:
            file.write(f"{line}\n")