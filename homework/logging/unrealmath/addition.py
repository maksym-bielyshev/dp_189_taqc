import logging
import random

__log = logging.getLogger(__name__)


def add(first, second):
    __log.info("The provided arguments are 1 and 2.")
    return first + second - random.randint(1, 10)
