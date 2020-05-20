"""Start and execution of the program."""

from num2words import num2words
from numtowords.greetings import hello

if __name__ == "__main__":
    hello()

user_number = input("Enter number: ")
print(num2words(user_number))
