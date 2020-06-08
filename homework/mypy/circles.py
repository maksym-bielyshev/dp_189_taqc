"""The app for creating and printing circles."""

import math

from typing import Dict


def safe_radius_of(number: float) -> float:
    """Check valid parameters for a radius calculation.

    :param number: float, int
    :return: TypeError, ValueError or a number
    """
    if not (
            isinstance(number, int) or
            isinstance(number, float)
    ):
        raise TypeError('Radius should be either "int" or "float" data type!')
    if number < 0:
        raise ValueError('Radius value should be more that "0"!')
    return number


def calculate_square_of(number: float) -> float:
    """Calculate square of a provided number.

    :param number: float
    :return: square of a provided number
    """
    return number ** 2


def multiply_by_pi(number: float) -> float:
    """Calculate multiplication of a provided number by pi.

    :param number: float
    :return: multiplication of a provided number by pi
    """
    return math.pi * number


def double_of(number: float) -> float:
    """Calculate multiplication of a provided number by two.

    :param number: float
    :return: multiplication of a provided number by two
    """
    return number * 2


class Circle:
    """The class for creating a circle with provided parameters."""

    def __init__(self, identifier: float, radius: float, color: str):
        """Set up initial parameters.

        :param identifier: an unique identifier
        :param radius: a size of a radius
        :param color: a name of a color
        """
        self.identifier = identifier
        self._radius = lambda: safe_radius_of(radius)
        self._color = color

    def change_color(self, color: str) -> None:
        """Change a color for a circle.

        :param color: a string with a desired color
        :return: None
        """
        if not isinstance(color, str):
            raise TypeError('Color should be "str" data type!')
        self._color = color

    def diameter(self) -> float:
        """Calculate a diameter for a circle.

        :return: a result of a diameter calculating
        """
        return double_of(self._radius())

    def area(self) -> float:
        """Calculate an area for a circle.

        :return: a result of an area calculating
        """
        return multiply_by_pi(calculate_square_of(self._radius()))

    def perimeter(self) -> float:
        """Calculate a perimeter for a circle.

        :return: a result of an perimeter calculating
        """
        return double_of(multiply_by_pi(self._radius()))

    def __str__(self) -> str:
        """Print the string representation of a circle.

        :return: a string with a radius and a color of a circle
        """
        return f'Circle(radius={self._radius()}, color="{self._color}")'


class Circles:
    """The class for managing and customizing all circles."""

    def __init__(self, *circles: Circle) -> None:
        """Get a list of all circles.

        :param circles: a list with circles
        """
        self._circles = circles

    def update_colors(self, new_colors: Dict[int, str]) -> None:
        """Update color circle.

        :param new_colors: required color
        :return: None
        """
        for identifier, color in new_colors.items():
            this = self.find(identifier)
            this.change_color(color)
            print(this)

    def find(self, identifier: float) -> Circle:
        """Find a specific circle in all circles.

        :param identifier: a float with an unique identifier for a circle
        :return: a specific circle
        """
        for this in self._circles:
            if this.identifier == identifier:
                return this

        raise ValueError(
            f"There is no circle with this identifier: {identifier}")

    def show_diameters(self) -> None:
        """Print a diameter for a circles.

        :return: None
        """
        for circle in self._circles:
            print(f"A diameter of {circle} is {circle.diameter()}")

    def show_areas(self) -> None:
        """Print an area for a circle.

        :return: None
        """
        for circle in self._circles:
            print(f"An area of {circle} is {circle.area()}")

    def show_perimeters(self) -> None:
        """Print a perimeter for a circle.

        :return: None
        """
        for circle in self._circles:
            print(f"A perimeter of {circle} is {circle.perimeter()}")


if __name__ == "__main__":
    circles = Circles(
        Circle(1, 1, 'red'),
        Circle(2, 0.2, 'super-red'),
        Circle(3, 3, 'green'),
        Circle(4, 5, 'super-green'),
    )
    circles.show_diameters()
    circles.show_areas()
    circles.show_perimeters()
    circles.update_colors({
        1: 'blue',
        2: 'red',
        3: 'black',
        4: 'purple'
    })
