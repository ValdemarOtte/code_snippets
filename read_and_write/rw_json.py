### Imports
# Standard library
from pathlib import Path
import json

# Third-party libraries

# Local files


def read_json(path: Path, encoding: str = "UTF-8") -> dict:
    """
    Read json-file and return it's content.

    :param Path path: Path to json-file.
    :param str encoding: Encoding for the json-file. Default is `UTF-8`.
    :return dict: A list of strings with the content of the file.
    """
    with open(path, "r", encoding=encoding) as file:
        return json.load(file)


def write_content_to_json(path: Path, content: dict, encoding: str = "UTF-8", mode: str = "w") -> None:
    """
    Write content to a json-file.

    Default mode is `w` (write).

    :param Path path: Path to json-file.
    :param dict content: The content which will be writed to the json-file.
    :param str encoding: Encoding for the json-file. Default is `UTF-8`.
    :param str mode: Mode for file. Default is `w`.
    """
    with open(path, mode=mode, encoding=encoding) as file:
        json.dump(content, file)
