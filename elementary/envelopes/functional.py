"""The application checks if one envelope can be nested in another."""


def check_nesting(first_envelope: tuple, second_envelope: tuple) -> str:
    """Check if one envelope can fit into another.

    :return: string with check result
    """
    if max(first_envelope) > max(second_envelope) and \
            min(first_envelope) > min(second_envelope):
        return "You can put the second envelope into the first one."

    elif max(first_envelope) < max(second_envelope) and \
            min(first_envelope) < min(second_envelope):
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
                print(check_nesting(first_envelope_user, second_envelope_user))

                run_app = input(
                    'Do you want to continue? "Yes" or "Y" '
                ).lower()
