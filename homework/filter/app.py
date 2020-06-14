"""Application for annotation and filtering text files."""

import sys
import os
from abc import ABC, abstractmethod


class Option(ABC):
    """Abstract class for creating options."""

    @abstractmethod
    def process_file(self, file) -> None:
        """Abstract method for processing the file.

        :param file: user provided file
        :return: processing result
        """
        pass

    @staticmethod
    def pick_option(option: str):
        """Pick an option.

        :param option: user provided option
        :return: class with option or error message
        """
        if option == "filter":
            return FilterOption()
        if option == "annotate":
            return AnnotationOption()
        else:
            print("No such option!")


class AnnotationOption(Option):
    """Annotation option class."""

    def process_file(self, file):
        """Annotate the provided file by the rules.

        :param file: user provided file
        :return: processing result
        """
        with open(file) as current_file:
            line_number = 1
            for line in current_file:
                line_result = [f"{str(line_number)}:"]
                for check in all_rules:
                    if check.check_rule(line):
                        line_result.append(check.get_annotation())
                print(" ".join(line_result))
                line_number += 1


class FilterOption(Option):
    """Filter option class."""

    def process_file(self, file):
        """Filter the provided file by the rules.

        :param file: user provided file
        :return: processing result
        """
        with open(file) as current_file:

            line_number = 1

            for line in current_file:
                line_result = [f"{str(line_number)}: "]

                number_display_rules = 0
                number_not_display_rules = 0

                for check in display_rules:
                    if check.check_rule(line):
                        number_display_rules += 1

                for check in not_display_rules:
                    if check.check_rule(line):
                        number_not_display_rules += 1

                if number_display_rules >= number_not_display_rules:
                    line_result.append(line)
                    print("".join(line_result))

                line_number += 1


class Rule(ABC):
    """Abstract class for creating rules."""

    @abstractmethod
    def get_annotation(self) -> str:
        """Provide a name of the rule (like FP005)."""
        pass

    @abstractmethod
    def check_rule(self, line: str) -> bool:
        """Return True if a given line matches the rule."""
        pass


class EndDot(Rule):
    """Rule: a line ends with a dot."""

    def get_annotation(self) -> str:
        """Provide a name of the rule.

        :return: rule name string
        """
        return "FP001"

    def check_rule(self, line: str) -> bool:
        """Return True if a given line matches the rule.

        :param line: text file line
        :return: boolean with answer about finding a match
        """
        return line.endswith(".")


class LessOneHundredChars(Rule):
    """Rule: a line is less than 100 characters."""

    def get_annotation(self) -> str:
        """Provide a name of the rule.

        :return: rule name string
        """
        return "FP002"

    def check_rule(self, line: str) -> bool:
        """Return True if a given line matches the rule.

        :param line: text file line
        :return: boolean with answer about finding a match
        """
        return 100 > len(line)


class AtLeastFiveALetters(Rule):
    """Rule: a line has at least 5 'a' letters."""

    def get_annotation(self) -> str:
        """Provide a name of the rule.

        :return: rule name string
        """
        return "FP003"

    def check_rule(self, line: str) -> bool:
        """Return True if a given line matches the rule.

        :param line: text file line
        :return: boolean with answer about finding a match
        """
        return line.count("a") > 4


class MoreThanThreeZLetters(Rule):
    """Rule: a line has more than 3 'z' letters."""

    def get_annotation(self) -> str:
        """Provide a name of the rule.

        :return: rule name string
        """
        return "FN201"

    def check_rule(self, line: str) -> bool:
        """Return True if a given line matches the rule.

        :param line: text file line
        :return: boolean with answer about finding a match
        """
        return line.count("z") > 3


class EmptyLine(Rule):
    """Rule: a line is empty."""

    def get_annotation(self) -> str:
        """Provide a name of the rule.

        :return: rule name string
        """
        return "FN202"

    def check_rule(self, line: str) -> bool:
        """Return True if a given line matches the rule.

        :param line: text file line
        :return: boolean with answer about finding a match
        """
        return line == "\n"


class NonLetterCharacters(Rule):
    """Rule: a line consists only from non-letter characters."""

    def get_annotation(self) -> str:
        """Provide a name of the rule.

        :return: rule name string
        """
        return "FN203"

    def check_rule(self, line: str) -> bool:
        """Return True if a given line matches the rule.

        :param line: text file line
        :return: boolean with answer about finding a match
        """
        return not line.isalpha()


display_rules = (
    EndDot(),
    LessOneHundredChars(),
    AtLeastFiveALetters()
)

not_display_rules = (
    MoreThanThreeZLetters(),
    EmptyLine(),
    NonLetterCharacters()
)

all_rules = (*display_rules, *not_display_rules)


if __name__ == "__main__":
    user_option = Option.pick_option(sys.argv[1])

    if os.path.exists(sys.argv[2]) and sys.argv[2].endswith(".txt"):
        user_option.process_file(sys.argv[2])
    else:
        print("No such file!")
