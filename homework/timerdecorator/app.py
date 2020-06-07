"""Demonstrate an example of how the function works with an error."""

from homework.timerdecorator.timer import timer


# @print_result_func
@timer
def division(dividend: int, divisor: int) -> float:
    """Divide and demonstrate the work of the timer.

    :param dividend: integer
    :param divisor: integer
    :return: float
    """
    return dividend / divisor


if __name__ == "__main__":
    division(1, 0)
