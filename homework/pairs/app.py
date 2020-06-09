"""The module with user input numbers and function for pairs search."""


def search_pairs(numbers: list, required_sum: int) -> list:
    """Search for pairs whose sum is equal to a required one.

    :param numbers: list of provided numbers
    :param required_sum: a number of required sum
    :return: list with suitable pairs
    """
    list_of_pairs = list()
    all_unique_numbers = set()

    for number_index in range(len(numbers)):
        suitable_pair = required_sum - numbers[number_index]
        if suitable_pair in all_unique_numbers:
            list_of_pairs.append(f'{numbers[number_index]} + {suitable_pair}')
        all_unique_numbers.add(numbers[number_index])
    return list_of_pairs


if __name__ == '__main__':
    run_app = 'y'
    while run_app == 'y':
        input_numbers = input('Please enter numbers with a space delimiter: ')
        input_required_sum = input("Please enter a required sum: ")

        try:
            numbers_int_list = [int(item) for item in input_numbers.split()]
            required_sum_int = int(input_required_sum)

        except ValueError:
            print("Please enter the correct data in the specified format!")

        else:
            result_list = search_pairs(numbers_int_list, required_sum_int)

            if result_list:
                for pair in result_list:
                    print(pair)
            else:
                print("Nothing found.")

        run_app = input("Do you want to continue? Y/N ").lower()
