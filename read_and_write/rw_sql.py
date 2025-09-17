### Imports
# Standard library
from pathlib import Path
import sqlite3

# Third-party libraries

# Local files


def read_db(path: Path, sql: str):
    """
    Read the database and return the wanted information.
    
    :param Path path: Path to database.
    :param str sql: The SQL statement.
    :return list: A list of the wanted information from the database.
    """
    with sqlite3.connect(path) as conn:
        cursor = conn.cursor()
        result = cursor.execute(sql)
        return [element for element in result.fetchall()]


def executre_sql_on_db(path: Path, sql: str) -> None:
    """
    Executre SQL statement on the database.

    :param Path path: Path to database.
    :param str sql: The SQL statement.
    """
    with sqlite3.connect(path) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
