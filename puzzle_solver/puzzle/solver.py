"""Aim: automate the process of solving puzzles Scroggs posts in Puzzle Village from his puzzle_solver webpage, i.e. http://mathoffstickerbook.com/sync/ehaftEyG7fPRFQE0ZJNG

This script contains the main routine that solves the puzzle_solver puzzle"""
from puzzle_solver.puzzle.utils import read_string, solve_puzzle


def solve_stickerbook_puzzle(puzzle_string: str) -> str:
    """
    Takes in the string describing the puzzle and outputs
    the solution, showing where to put the digits 1-9.
    puzzle_string: string specifying puzzle
    return: string giving the solution
    """
    processed_puzzle = read_string(puzzle_string)
    solved_puzzle = solve_puzzle(processed_puzzle)

    return solved_puzzle


if __name__ == "__main__":
    puzzle_string = """
plus plus 11
plus plus 17
plus plus 17
plus times 11
times minus 17
times plus 17
"""

    print("Inputted puzzle:")
    print(puzzle_string)

    solved_puzzle = solve_stickerbook_puzzle(
        puzzle_string=puzzle_string
    )

    print(solved_puzzle)
