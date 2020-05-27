def search_pairs(numbers: list, required_sum: int) -> list:
    """Searching for pairs whose sum is equal to a required one."""
    #todo docstring returning values with exception

    list_of_pairs = []
    all_numbers = set()
    for i in range(0, len(numbers)):
        suitable_pair = required_sum - numbers[i]
        if suitable_pair in all_numbers:
            list_of_pairs.append(f'{suitable_pair} + {numbers[i]}')
        all_numbers.add(numbers[i])
    return list_of_pairs


if __name__ == '__main__':
    numbers = [int(item) for item in input('Enter numbers: ').split()]
    required_sum = int(input('Enter required sum: '))
    print(search_pairs(numbers, required_sum))
