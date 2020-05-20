def get_stats():
    """Statistic about given file: number of lines, number of empty lines,
    number of lines with 'z', number of 'z' letter, number of lines with 'and'"""

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
    """Making a decision to repeat or stop the program."""

    while True:
        print(get_stats())
        answer = input('Do you want to analyze another file? y/n: ').lower()
        if answer != 'y':
            print('Goodbye!')
            break


if __name__ == '__main__':
    execution()
