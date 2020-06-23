def search_palindromes(number):
    len_number = len(number)
    second_index = 2
    palindromes = set()

    while True:

        first_index = 0
        iteration_counter = 0

        while second_index <= len_number:

            if number[first_index:second_index] == number[first_index:second_index][::-1]:
                palindromes.add(number[first_index:second_index])
            first_index += 1
            second_index += 1
            iteration_counter += 1

        second_index = second_index - iteration_counter + 1

        if second_index > len_number:
            break

    return palindromes


number = '1234437'

result = search_palindromes(number)

if result:
    print(f"Palindromes in {number}:")
    for palindrome in result:
        print(palindrome)
else:
    print("No palindromes found.")
