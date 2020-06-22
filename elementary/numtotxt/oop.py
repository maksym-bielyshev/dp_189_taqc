"""The application converts an integer into a text representation."""

from num2words import num2words


class FixNum2Words:
    """Class with fixed 'num2words' module."""

    @staticmethod
    def add_minus_ru(func):
        """Convert number to the string representation.

        :return: decorated function
        """
        def wrapper(number):
            """Adding a minus in Russian for a number in the range of 0 and -1.

            :param number: string as a float number
            :return: new fixed behavior for a decorated function
            """
            if 0 > float(number) > -1:
                number_without_minus = str(number).lstrip("-")
                text_representation_without_minus = \
                    func(number_without_minus, lang='ru')
                return f"минус {text_representation_without_minus}"

            else:
                return func(number, lang='ru')

        return wrapper


if __name__ == "__main__":

    print(__doc__)

    num2words = FixNum2Words.add_minus_ru(num2words)

    run_app = "y"
    while run_app == "y" or run_app == "yes":
        user_number = input("Please enter the number: ")
        print(num2words(user_number))

        run_app = input("Do you want to continue? "
                        "If yes, enter 'yes' or 'y': ")
