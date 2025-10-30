### Imports
# Standard library

# Third-party libraries

# Local files


def convert_danish_floats_to_floats(number: str) -> float:
    """
    Convert danish floats to float, so the machine can read it.

    e.x. "5.713.291,95" (str) will be converted to "5713291.95" (float).
    
    :param str number: The danish number as a string.
    :return float: The number as a float.
    """
    number = number.replace(".", "")
    number = number.replace(",", ".")
    return float(number)


def convert_floats_to_danish_floats(number: float) -> str:
    """
    Convert floats to more readable floats with the danish system for numbers.
    
    e.x. "5713291.95" (float) will be converted to "5.713.291,95" (str).
    
    :param float number: The number as a float.
    :return str: The danish number as a string.
    """
    numbers, d = str(number).split(".")
    nss = []
    for i, n in enumerate(list(numbers)[::-1]):
        if i % 3 == 0:
            nss.append(".")
        nss.append(n)
    return "".join(nss[1:][::-1]) + "," + d
