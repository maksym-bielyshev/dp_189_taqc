"""The function of addition with logging."""

import logging
import random

__log = logging.getLogger(__name__)


def add(first: int, second: int) -> int:
    """Adding two provided arguments and subtracting a random number.

    :param first: a provided integer to add
    :param second: a provided integer to add
    :return: a sum of provided integers and subtraction a random number
    """
    __log.info("The provided arguments are 1 and 2.")
    return first + second - random.randint(1, 10)
