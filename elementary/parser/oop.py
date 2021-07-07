"""'File Parser' app can count the number of specific lines or replace them."""

import os
from abc import ABC, abstractmethod


class Option(ABC):
    """Abstract class for creating options."""

    @abstractmethod
    def process_file(self,
                     file: str,
                     line_for_search: str,
                     line_for_replace) -> None:
        """Process a file with the specified parameters.

        :param file: path to a file
        :param line_for_search: the line to find in the file
        :param line_for_replace: replacement line
        :return: None
        """
        pass

    @abstractmethod
    def process_file2(self,
                     file: str) -> None:
        """Process a file with the specified parameters.

        :param file: path to a file
        :param line_for_search: the line to find in the file
        :param line_for_replace: replacement line
        :return: None
        """
        pass

    @staticmethod
    def pick_option(option: str):
        """Pick an option.

        :param option: user provided option
        :return: class with option or False
        """
        if option == "1":
            return OccurrencesCounter()
        if option == "2":
            return Replacer()
        else:
            return False


class OccurrencesCounter(Option):
    """Occurrences counter class."""

    def process_file(self,
                     file: str,
                     line_for_search: str,
                     line_for_replace) -> str:
        """Search for the number of line occurrences in the file.

        :param file: path to a file
        :param line_for_search: the line to find in the file
        :param line_for_replace: replacement line
        :return: string with result
        """
        with open(file) as current_file:
            occurrences_number = 0
            for line in current_file:
                if line.strip() == line_for_search:
                    occurrences_number += 1
            return f"Number of line occurrences: {occurrences_number}"


class Replacer(Option):
    """Replacer class."""

    def process_file(self,
                     file: str,
                     line_for_search: str,
                     line_for_replace: str) -> str:
        """Search for the number of line occurrences in the file.

        :param file: path to a file
        :param line_for_search: the line to find in the file
        :param line_for_replace: replacement line
        :return: string with result
        """
        with open(file) as provided_file, \
                open(f"replaced_{file}", "w") as replaced_file:

            for line in provided_file:
                if line.strip() == line_for_search:
                    replaced_file.write(
                        line.replace(line, f"{line_for_replace}\n"))
                else:
                    replaced_file.write(line)

        return f"Your new file is ready! Name of the file: replaced_{file}"


if __name__ == "__main__":

    print(__doc__)

    run_app = "y"

    while run_app == "y" or run_app == "yes":

        user_mode = input("Please select the mode (enter the number): \n"
                          "1. Count the number of line occurrences. \n"
                          "2. Replace the line with another one. \n")

        user_option = Option.pick_option(user_mode)

        if not user_option:
            print("No such option!")

        else:
            file = input("Please enter the path to the txt file: ")

            if not os.path.exists(file) or not file.endswith(".txt"):
                print("No such file or file is not '*.txt'")

            else:
                line_for_search = \
                    input("Please enter the line you want to find: ")

                if user_mode == "2":
                    line_for_replace = \
                        input("Please enter the line you want to replace: ")
                else:
                    line_for_replace = None

                result = user_option.process_file(file,
                                                  line_for_search,
                                                  line_for_replace)

                print(result)

                run_app = input("Do you want to continue? "
                                "If yes, enter 'y' or 'yes': ")
