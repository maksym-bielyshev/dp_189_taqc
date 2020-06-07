"""Decorators for timer and display of final result."""

import functools
import time


def timer(function):
    """Print the runtime of the decorated function.

    :param function: some function to calculate time
    :return: string with the time for the function duration
    """
    @functools.wraps(function)
    def wrapper_timer(*args, **kwargs):

        start_time = time.perf_counter()

        try:
            value = function(*args, **kwargs)

        except BaseException as e:
            raise e

        finally:
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {function.__name__!r} in {run_time:.7f} secs \n")

        return value

    return wrapper_timer


def print_result_func(func):
    """Print the final result.

    :param func:
    :return: result string
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        try:
            value = func(*args, **kwargs)
            result = f"{value}"

        except BaseException as e:
            raise e
            result = f"An exception occurred! Info about the exception: {e}"
            value = None

        print(result)
        return value

    return wrapper
