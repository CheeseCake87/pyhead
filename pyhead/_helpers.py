from random import choices
from string import ascii_letters, digits
from typing import Union, Optional


def random_key(append: Optional[Union[str, int]] = None) -> str:
    """
    Generate a random string used in element keys.

    Returns:
        str: Random string of given length.
    """
    return (
        "".join(choices(ascii_letters + digits, k=12)) + str(append)
        if append
        else "".join(choices(ascii_letters + digits, k=12))
    )
