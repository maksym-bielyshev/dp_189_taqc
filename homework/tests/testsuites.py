"""Creating and running the test suite."""

import unittest
from testcases import TestAdd, TestSubtract


def suite():
    """Create the test suite with the required tests."""
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_at_least_one_argument_is_zero"))
    suite.addTest(TestAdd("test_all_arguments_are_less_than_zero"))
    suite.addTest(TestSubtract("test_at_least_one_argument_is_zero"))
    suite.addTest(TestSubtract("test_all_arguments_are_less_than_zero"))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
