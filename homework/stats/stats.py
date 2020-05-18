def stats():
    file = input("File: ")
    lines = 0
    empty_lines = 0
    z_lines = 0
    z_letters = 0
    and_lines = 0

    with open(file, 'r') as f:
        for line in f:
            lines += 1

            if line == '\n':
                empty_lines += 1

            if 'z' in line:
                z_lines += 1

            for char in line:
                if char == 'z':
                    z_letters += 1

            if 'and' in line:
                and_lines += 1

        print(f"total lines: {lines}")
        print(f"empty lines: {empty_lines}")
        print(f"lines with 'z': {z_lines}")
        print(f"'z' count': {z_letters}")
        print(f"lines with 'and': {and_lines}")


if __name__ == '__main__':
    stats()
