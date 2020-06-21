"""Application for sorting triangles by their area."""

import math


class Triangle:
    """Create a triangle and calculate an area."""

    def __init__(self,
                 name: str,
                 first_side: float,
                 second_side: float,
                 third_side: float):
        """Create a triangle.

        :param name: name from user
        :param first_side: side size from user
        :param second_side: side size from user
        :param third_side: side size from user
        """
        self.name = name
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        self.area = None

    def calculate_triangle_area(self) -> float:
        """Calculate a triangle area.

        :return: float with a triangle area
        """
        half_perimeter = 0.5 * (self.first_side
                                + self.second_side
                                + self.third_side)

        self.area = math.sqrt(
            half_perimeter
            * (half_perimeter - self.first_side)
            * (half_perimeter - self.second_side)
            * (half_perimeter - self.third_side)
        )

        return self.area


if __name__ == "__main__":

    print(__doc__)

    triangles_names_areas = {}

    run_app = "y"
    while run_app == "y" or run_app == "yes":

        user_input = input('Enter a name of a triangle and three sizes '
                           'with a semicolon and a space delimiter: ')

        try:
            formatted_data = user_input.replace(' ', '').split(',')
            name_user = formatted_data[0]
            first_size_user = float(formatted_data[1])
            second_size_user = float(formatted_data[2])
            third_size_user = float(formatted_data[3])

        except(ValueError, IndexError):
            print("Please enter valid data in correct format!")

        else:
            example = Triangle(name_user,
                               first_size_user,
                               second_size_user,
                               third_size_user)

            example.calculate_triangle_area()

            triangles_names_areas[example.name] = example.area

            another_triangle_answer = \
                input("Do you want to add another triangle? "
                      "If yes, please enter 'yes' or 'y' ")

            if another_triangle_answer != "y":

                sort_triangles = sorted(
                    triangles_names_areas.items(),
                    key=lambda x: x[1],
                    reverse=True
                )

                print("============= Triangle list: ===============")
                row_number = 1
                for item in sort_triangles:
                    print(f"{row_number}. [Triangle {item[0]}]: {item[1]} cm")
                    row_number += 1

                break
