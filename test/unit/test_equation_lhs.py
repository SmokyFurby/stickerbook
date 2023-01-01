import unittest

from stickerbook_puzzle_solver.equation_lhs import RowOrColumn


class TestRowOrColumn(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = RowOrColumn()
        self.number_1 = 1
        self.operation_1 = "+"
        self.number_2 = 3
        self.operation_2 = "/"
        self.number_3 = 2
        self.output = 2

    def test_should_build_equation(self):
        expected = True
        actual = self.sut.build_equation(
            self.number_1,
            self.operation_1,
            self.number_2,
            self.operation_2,
            self.number_3,
            self.output
        )

        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, bool)
        self.assertEqual(expected, actual)

    def test_should_check_equals(self):
        self.sut._lhs = self.output

        expected = False

        actual = self.sut.check_equals(3)

        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, bool)
        self.assertEqual(expected, actual)

    def test_should_build_lhs(self):
        self.sut.build_lhs(
            self.number_1,
            self.operation_1,
            self.number_2,
            self.operation_2,
            self.number_3
        )

        expected = 2
        actual = self.sut._lhs

        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

    def test_should_apply_string_operation(self):
        expected = 4

        actual = self.sut.apply_string_operation(
            self.number_1,
            self.operation_1,
            self.number_2
        )

        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)