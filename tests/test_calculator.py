"""Unit tests for the example service.

Green on the clean baseline (AC-2, AC-3). The AC-5 case patch breaks ``add`` so
``test_add`` fails, which fails the Flow B test stage and triggers the SNS
failure notification (AC-5).
"""

import unittest

from example_service.calculator import add, multiply, subtract


class CalculatorTest(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)


if __name__ == "__main__":
    unittest.main()
