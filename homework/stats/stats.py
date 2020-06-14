"""Get the statistics about the file and decide on the repetition."""


def get_stats() -> dict:
    """Get required statistic about given file.

    :return: dictionary with statistic result
    """
    file = input("File: ")

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

        result = get_stats()
        for item in result:
            print(f"{item}: {result[item]}")

        run_app = input('Do you want to analyze another file? y/n: ').lower()
