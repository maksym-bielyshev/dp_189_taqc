"""Conversion function provided number to the string representation."""

from num2words import num2words


def num2words_fixed_minus_zero_one(func):
    """Convert number to the string representation.

    :return: decorated function
    """
    def wrapper(number):
        """Adding a minus for a number in the range of 0 and -1.

        :param number: string as a float number
        :return: new fixed behavior for a decorated function
        """
        if 0 > float(number) > -1:
            number_without_minus = str(number).lstrip("-")
            text_representation_without_minus = func(number_without_minus)
            return f"minus {text_representation_without_minus}"

        else:
            return func(number)

    return wrapper


num2words = num2words_fixed_minus_zero_one(num2words)
