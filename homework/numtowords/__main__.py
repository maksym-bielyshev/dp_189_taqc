"""Start and execution of the program with all imported modules."""


from numtowords.instruction import instruction
from numtowords.num_to_words_converter import num2words_fixed_minus_zero_one

if __name__ == "__main__":
    print(instruction())
    print(num2words_fixed_minus_zero_one())
