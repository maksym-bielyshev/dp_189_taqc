"""Get the statistics about the file and decide on the repetition."""


def get_stats() -> dict:
    """Get required statistic about given file.

    :return: dict
    """
    file = input("File: ")

    dict_result = {
        'total_lines': 0,
        'empty_lines': 0,
        'z_lines': 0,
        'z_letters': 0,
        'and_lines': 0
    }

    with open(file, 'r') as f:
        for line in f:
            dict_result['total_lines'] += 1

            if line == '\n':
                dict_result['empty_lines'] += 1

            if 'z' in line:
                dict_result['z_lines'] += 1

            if 'and' in line:
                dict_result['and_lines'] += 1

            dict_result['z_letters'] += line.count('z')

        return dict_result


def execution():
    """Make a decision to repeat or stop the program.

    :return: function get_stats() or break
    """
    while True:
        print(get_stats())
        answer = input('Do you want to analyze another file? y/n: ').lower()
        if answer != 'y':
            print('Goodbye!')
            break


if __name__ == '__main__':
    execution()
