def stats():
    """Statistic about given file: number of lines, number of empty lines,
    number of lines with 'z', number of 'z' letter, number of lines with 'and'"""

    file = input("File: ")

    all_lines = 0
    empty_lines = 0
    z_lines = 0
    z_letters = 0
    and_lines = 0

    with open(file, 'r') as f:
        for line in f:
            all_lines += 1

            if line == '\n':
                empty_lines += 1

            if 'z' in line:
                z_lines += 1

            for char in line:
                if char == 'z':
                    z_letters += 1

            if 'and' in line:
                and_lines += 1

        list_result = [f"total lines: {all_lines}",
                       f"empty lines: {empty_lines}",
                       f"lines with 'z': {z_lines}",
                       f"'z' count': {z_letters}",
                       f"lines with 'and': {and_lines}"]

        return list_result


def execution():
    """Making a decision to repeat or stop the program."""

    condition = 1
    while condition:
        print(stats())
        answer = input('Do you want ot analyze another file? y/n: ').lower()
        if answer == 'y':
            condition = 1
        else:
            condition = 0
            print('Goodbye!')


if __name__ == '__main__':
    execution()
