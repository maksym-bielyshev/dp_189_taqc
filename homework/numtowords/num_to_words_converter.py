"""Conversion function provided number to the string representation."""

from num2words import num2words


def num2words_fixed_minus_zero_one(func):
    """Convert number to the string representation.

    :return: string with result
    """
    def wrapper(number):
        if 0 > float(number) > -1:
            number_without_minus = str(number).lstrip("-")
            text_representation_without_minus = func(number_without_minus)
            return f"minus {text_representation_without_minus}"

        else:
            return func(number)

    return wrapper


num2words = num2words_fixed_minus_zero_one(num2words)
