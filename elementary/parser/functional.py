"""'File Parser' app can count the number of specific lines or replace them."""

import os


def pick_option(option):
    """Pick an option.

    :param option: user provided option
    :return: function with option or False
    """
    if option == "1":
        return occurrences_counter
    if option == "2":
        return replacer
    else:
        return False


def occurrences_counter(file: str,
                        line_for_search: str,
                        line_for_replace = None) -> str:
    """Search for the number of line occurrences in the file.

    :param file: path to a file
    :param line_for_search: the line to find in the file
    :param line_for_replace: replacement line (if provided)
    :return: string with result
    """
    with open(file) as current_file:
        occurrences_number = 0
        for line in current_file:
            if line.strip() == line_for_search:
                occurrences_number += 1
        return f"Number of line occurrences: {occurrences_number}"


def replacer(file: str,
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

    return f"Your new file is ready! Name of the file: (replaced_{file})"


if __name__ == "__main__":

    print(__doc__)

    run_app = "y"

    while run_app == "y" or run_app == "yes":

        user_mode = input("Please select the mode (enter the number): \n"
                          "1. Count the number of line occurrences. \n"
                          "2. Replace the line with another one. \n")

        picked_option = pick_option(user_mode)

        if not picked_option:
            print("No such option!")

        else:
            file = input("Please enter the path to the txt file: ")

            if not os.path.exists(file) or not file.endswith(".txt"):
                print("No such file or file is not '*.txt'")

            else:
                line_for_search = \
                    input("Please enter the line you want to find: ")

                line_for_replace = None

                if user_mode == "2":
                    line_for_replace = \
                        input("Please enter the line you want to replace: ")

                result = picked_option(file,
                                       line_for_search,
                                       line_for_replace)

                print(result)

                run_app = input("Do you want to continue? "
                                "If yes, enter 'y' or 'yes': ")
