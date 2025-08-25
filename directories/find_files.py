### Imports
# Standard library
import os
from pathlib import Path

# Third-party libraries

# Local files


def files_from_directory(path: Path) -> list[Path]:
    """
    Get relative paths for all files from a direcetory.

    :param Path path: Path to directory.
    :return list[str]: A list of relative paths for all the files in the directory.
    """
    return [Path(path / file) for file in os.listdir(path)]


def files_from_directory_with_wanted_extension(path: Path, extension: str) -> list[Path]:
    """
    Get relative paths for all files from a direcetory with an wanted extension.

    :param Path path: Path to directory.
    :param str extension: The wanted extension for files.
    :return list[str]: A list of relative paths for all the files in the directory with an wanted extension.
    """
    return [Path(path / file) for file in os.listdir(path) if file.endswith(extension)]
