"""CLI app for solving the sticker book puzzle"""

import click

from stickerbook_puzzle_solver.domain.stickerbook_puzzle import StickerbookPuzzleSolver


@click.command()
@click.option('--puzzle_path', help='Full filepath to txt file containing puzzle')
def cli_app(puzzle_path: str):
    with open(puzzle_path, 'r') as reader:
        puzzle_string = reader.read()

    print("Inputted puzzle:")
    puzzle = StickerbookPuzzleSolver(puzzle_string)

    print(puzzle_string)

    solved_puzzle = puzzle.solve()

    print("The solution is:")
    print(solved_puzzle)
