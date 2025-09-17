### Imports
# Standard library
from pathlib import Path
import csv

# Third-party libraries

# Local files


def read_csv(path: Path, encoding: str = "UTF-8", header: bool = True) -> tuple[list[str], list[list[str]]]:
    """
    Read csv-file and return the header and its content.

    :param Path path: Path to csv-file.
    :param str encoding: Encoding for the csv-file. Default is `UTF-8`.
    :param bool header: Bool value whether the csv-file contains a header or not. Default is `True`.
    :return tuple[list[str], list[list[str]]]: A tuple with the header and content of the csv-file.
    """
    with open(path, "r", encoding=encoding) as file:
        csvreader = csv.reader(file)
        if header:
            fields = next(csvreader)
        rows = [row for row in csvreader]
        return fields, rows
    

def write_csv(path: Path, fields: list[str], rows: list[list[str]], encoding: str = "UTF-8", mode: str = "w") -> None:
    """"""
    if mode == "w":
        rows = [fields] + rows
    with open(path, mode=mode, encoding=encoding, newline="\n") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(rows)
