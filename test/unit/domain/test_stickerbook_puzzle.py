import unittest
from pathlib import Path

import numpy as np

from stickerbook_puzzle_solver.domain.stickerbook_puzzle import StickerbookPuzzleSolver


class TestStickerbookPuzzleSolver(unittest.TestCase):
    def setUp(self) -> None:
        self.puzzle_path = Path(__file__).parents[2].joinpath("common", "test_input.txt").as_posix()

        with open(self.puzzle_path, 'r') as reader:
            self.puzzle_string = reader.read()

        self.sut = StickerbookPuzzleSolver(self.puzzle_string)

        self.solution_string = '6 3 2\n5 8 4\n1 7 9'
        self.puzzle_array = [
            ["+", "+", 11],
            ["+", "+", 17],
            ["+", "+", 17],
            ["+", "*", 11],
            ["*", "-", 17],
            ["*", "+", 17],
        ]
        self.solution_array = np.array([[6,3,2],[5,8,4],[1,7,9]])

    def test_should_initialise(self):
        self.assertIsInstance(self.sut._puzzle_string, str)
        self.assertEqual(self.sut._puzzle_string, self.puzzle_string)
        self.assertIsNone(self.sut._puzzle)
        self.assertIsNone(self.sut._solution)

    def test_should_solve(self):
        actual = self.sut.solve()

        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, str)
        self.assertEqual(self.solution_string , actual)

    def test_should_read_string(self):
        actual = self.sut.read_string()

        self.assertIsNotNone(actual)
        self.assertListEqual(self.puzzle_array, actual)

    def test_should_seek_solution(self):
        self.sut._puzzle = self.puzzle_array

        actual = self.sut.seek_solution()

        self.assertIsNotNone(self.solution_string , actual)
        self.assertEqual(self.solution_string, actual)

    def test_should_convert_array_to_string(self):
        self.sut._solution = self.solution_array
        actual = self.sut.solution_array_to_string()

        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, str)
        self.assertEqual(self.solution_string, actual)
