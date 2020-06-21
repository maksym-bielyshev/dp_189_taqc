"""Enter height and width, the application will create a chessboard."""


class Chessboard:
    """Class to create a chessboard."""

    def __init__(self, height: int, width: int):
        """Height and width values from the user.

        :param height: integer
        :param width: integer
        """
        self.height = height
        self.width = width

    def create_chessboard(self) -> list:
        """Create a chessboard by specified parameters.

        :return: list with lines to print a chessboard
        """
        chessboard_list = []
        for index in range(self.height):
            if index % 2 == 0:
                chessboard_list.append(self.width * "* ")
            else:
                chessboard_list.append(self.width * " *")
        return chessboard_list


if __name__ == "__main__":
    print(__doc__)
    run_app = "y"
    while run_app == "y":

        height_str = input("Please enter the height: ")
        width_str = input("Please enter the width: ")

        try:
            height_int = int(height_str)
            width_int = int(width_str)

        except ValueError:
            print("Please enter only numbers!")

        else:
            if height_int > 0 and width_int > 0:
                example = Chessboard(height_int, width_int)
                for item in example.create_chessboard():
                    print(item)
            else:
                print("Please try to enter numbers above zero.")

        run_app = input("Do you want to continue? Y/N ")
