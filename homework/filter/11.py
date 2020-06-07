from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        pass

    @abstractmethod
    def matches(self, line: str) -> bool:
        """Returns True if a given line matches the filter, otherwise,
        returns False."""
        pass


class IsEndDot(Filter):
    def name(self) -> str:
        return "FP001"

    def matches(self, line: str) -> bool:
        return line.endswith(".") is True


class IsLessOneHundredChars(Filter):
    def name(self) -> str:
        return "FP002"

    def matches(self, line: str) -> bool:
        return 100 > len(line)


child_classes = (
    IsEndDot(),
    IsLessOneHundredChars()
)


if name == "main":

    # filter
    with open("test_file.txt") as f:
        line_number = 1
        for line in f:
            stripline = line.strip()
            line_result = [str(line_number), ": "]
            for check in child_classes:
                if check.matches(stripline):
                    line_result.append(stripline)
                    print("".join(line_result))
                    break
            line_number += 1

    # annotation
    with open("test_file.txt") as f:
        line_number = 1
        for line in f:
            stripline = line.strip()
            line_result = [f"{str(line_number)}"":"]
            for check in child_classes:
                if check.matches(stripline):
                    line_result.append(check.name())
            print(" ".join(line_result))
            line_number += 1
