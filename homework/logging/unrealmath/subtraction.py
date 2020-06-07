import logging
import random

__log = logging.getLogger(__name__)


def reduce(minuend, subtrahend):
    __log.info("The provided arguments are 2 and 1.")
    return minuend - subtrahend + random.randint(1, 10)
