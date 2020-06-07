"""Conversion function provided number to the string representation."""

from num2words import num2words


def converter() -> str:
    """Convert number to the string representation.

    :return: string with result
    """
    user_provided_number = input("Enter the number: ")

    try:
        return num2words(user_provided_number)
    except:
        return "Please enter only the number!"
