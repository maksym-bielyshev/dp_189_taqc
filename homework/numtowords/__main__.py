"""Start and execution of the program with all imported modules."""


from numtowords.instruction import instruction
from numtowords.num_to_words_converter import num2words_fixed_minus_zero_one

if __name__ == "__main__":
    run_app = 'y'
    while run_app == 'y':
        print(instruction())

        user_input_number = input("Enter the number: ")

        try:
            print(num2words_fixed_minus_zero_one(user_input_number))
        except ValueError:
            print("Please enter only the number!")

        run_app = input("Do you want to continue? Y/N ").lower()
