"""Conversion function provided number to the string representation."""

from num2words import num2words


def num2words_fixed_minus_zero_one() -> str:
    """Convert number to the string representation.

    :return: string with result
    """
    user_input_number = input("Enter the number: ")

    try:
        if 0 > float(user_input_number) > -1:
            number_without_minus = user_input_number.lstrip("-")
            text_representation_without_minus = num2words(number_without_minus)
            return f"minus {text_representation_without_minus}"

        else:
            return num2words(user_input_number)

    except ValueError:
        return f"Please enter only the number!"
