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

        print(f"total lines: {all_lines}")
        print(f"empty lines: {empty_lines}")
        print(f"lines with 'z': {z_lines}")
        print(f"'z' count': {z_letters}")
        print(f"lines with 'and': {and_lines}")

        def another_file_question():
            """Analyzing another file or ending a program."""

            answer = input("Do you want to analyze another file? y/n: ")
            if answer == 'Y' or answer == 'y':
                stats()
            else:
                print('Goodbye!')

        another_file_question()


if __name__ == '__main__':
    stats()
