"""The application checks if one envelope can be nested in another."""


class EnvelopeAnalysis:
    """Nesting check with sides provided from a user."""

    def __init__(self, first_envelope: tuple, second_envelope: tuple):
        """Create envelopes.

        :param first_envelope: tuple with the first envelope sizes
        :param second_envelope: tuple with the second envelope sizes
        """
        self.first_envelope = first_envelope
        self.second_envelope = second_envelope

    def check_nesting(self) -> str:
        """Check if one envelope can fit into another.

        :return: string with check result
        """
        if max(self.first_envelope) > max(self.second_envelope) and \
                min(self.first_envelope) > min(self.second_envelope):
            return "You can put the second envelope into the first one."

        elif max(self.first_envelope) < max(self.second_envelope) and \
                min(self.first_envelope) < min(self.second_envelope):
            return "You can put the first envelope into the second one."
        else:
            return "You can't put the envelope into another."


if __name__ == '__main__':
    print(__doc__)
    run_app = "y"
    while run_app == "y" or run_app == "yes":
        try:
            first_side_first_envelope = float(input(
                'Please enter the first side of the first envelope: '))
            second_side_first_envelope = float(input(
                'Please enter the second side of the first envelope: '))
            first_side_second_envelope = float(input(
                'Please enter the first side of the second envelope: '))
            second_side_second_envelope = float(input(
                'Please enter the second side of the second envelope: '))

        except(TypeError, ValueError):
            print('Please enter only numbers!')

        else:
            first_envelope_user = (first_side_first_envelope,
                                   second_side_first_envelope)
            second_envelope_user = (first_side_second_envelope,
                                    second_side_second_envelope)

            if min(first_envelope_user) < 0 or min(second_envelope_user) < 0:
                print("Please enter only positive numbers.")

            else:
                example = EnvelopeAnalysis(first_envelope_user,
                                           second_envelope_user)

                print(example.check_nesting())

                run_app = input('Do you want to continue? If yes, please '
                                'enter "Yes" or "Y" ').lower()
