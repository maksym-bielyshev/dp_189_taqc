"""The function of subtraction with logging."""

import logging
import random

__log = logging.getLogger(__name__)


def reduce(minuend: int, subtrahend: int) -> int:
    """Adding two provided arguments and subtracting a random number.

    :param first: a provided integer to add
    :param second: a provided integer to add
    :return: a sum of provided integers and addition a random number
    """
    __log.info("The provided arguments are 2 and 1.")
    return minuend - subtrahend + random.randint(1, 10)
