"""The module with user input numbers and function for pairs search."""


def search_pairs(numbers: list) -> list:
    """Search for pairs whose sum is equal to a required one.

    :param numbers: list of provided number
    :return: list
    """
    REQUIRED_SUM = 10

    list_of_pairs = []
    all_uniqal_numbers = set()

    for number_index in range(0, len(numbers)):
        suitable_pair = REQUIRED_SUM - numbers[number_index]
        if suitable_pair in all_uniqal_numbers:
            list_of_pairs.append(f'{suitable_pair} + {numbers[number_index]}')
        all_uniqal_numbers.add(numbers[number_index])
    return list_of_pairs


if __name__ == '__main__':
    try:
        user_numbers_list = [int(item) for item in input(
            'Hello! Please enter numbers with a space delimiter: ').split()]

    except ValueError as e:
        print(f"Please enter valid numbers! {e}")

    else:
        for pair in search_pairs(user_numbers_list):
            print(pair)

        if not search_pairs(user_numbers_list):
            print("Nothing found.")
