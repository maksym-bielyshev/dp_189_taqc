"""Demonstrate an example of how the function works with an error."""

from homework.timerdecorator.timer import timer, print_result_func


@print_result_func
@timer
def division(dividend: int, divisor: int) -> float:
    """Divide and demonstrate the result of the timer.

    :param dividend: integer dividend
    :param divisor: integer divisor
    :return: float result
    """
    return dividend / divisor


if __name__ == "__main__":
    division(1, 0)
