"""Get the statistics about the file and decide on the repetition."""

import os


def get_stats(file) -> dict:
    """Get required statistic about given file.

    :return: dictionary with statistic result
    """
    result_dict = {
        'total_lines': 0,
        'empty_lines': 0,
        'z_lines': 0,
        'z_letters': 0,
        'and_lines': 0
    }

    with open(file) as f:
        for line in f:
            result_dict['total_lines'] += 1

            if line == '\n':
                result_dict['empty_lines'] += 1

            if 'z' in line:
                result_dict['z_lines'] += 1

            if 'and' in line:
                result_dict['and_lines'] += 1

            result_dict['z_letters'] += line.count('z')

        return result_dict


if __name__ == '__main__':

    run_app = "y"
    while run_app == "y":

        user_file = input("Please enter a name of the file: ")

        if os.path.exists(user_file) and user_file.endswith(".txt"):
            result = get_stats(user_file)
            for item in result:
                print(f"{item}: {result[item]}")

        else:
            print("Wrong name or path, please try again!")

        run_app = input('Do you want to analyze another file? y/n: ').lower()
