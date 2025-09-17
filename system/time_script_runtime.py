### Imports
# Standard library
from datetime import datetime
from time import sleep

# Third-party libraries

# Local files


def measure_runtime(func):
    """
    A decorator to measure the runtime of a given function.
    """
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"Script runtime: {end - start}")
    return wrapper
