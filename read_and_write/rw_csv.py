### Imports
# Standard library
from pathlib import Path
import csv

# Third-party libraries

# Local files


def read_csv(path: Path, encoding: str = "UTF-8") -> list[str]:
    """
    Read txt-file and return lines.

    :param Path txt_path: Path to txt-file.
    :param str encoding: Encoding for the txt-file. Default is 'UTF-8'.
    :return list[str]: A list of strings with the content of the file.
    """
    with open(path, 'r') as file:
        csvreader = csv.reader(file, encoding=encoding)
