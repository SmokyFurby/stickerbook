from pathlib import Path
from unittest import TestCase

from stickerbook_puzzle_solver.domain.stickerbook_puzzle import StickerbookPuzzleSolver


class TestStickerBook(TestCase):
    def setUp(self) -> None:
        #arrange
        puzzle_path = Path(__file__).parents[1].joinpath("common", "test_input.txt").as_posix()

        with open(puzzle_path, "r") as reader:
            puzzle_string = reader.read()

        self.sut = StickerbookPuzzleSolver(puzzle_string)

    def test_should_solve_puzzle(self):
        # act
        solved_puzzle = self.sut.solve()

        #assert
        self.assertIsInstance(solved_puzzle, str)

        self.assertEqual(solved_puzzle, "6 3 2\n5 8 4\n1 7 9")
