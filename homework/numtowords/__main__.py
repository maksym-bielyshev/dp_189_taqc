"""Start and execution of the program with all imported modules."""


from numtowords.instruction import instruction
from numtowords.num_to_words_converter import converter, num2words

if __name__ == "__main__":
    print(instruction())
    print(converter())
