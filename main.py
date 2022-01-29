"""Aim: automate the process of solving puzzles Scroggs posts in Puzzle Village from his puzzle_solver webpage, i.e. http://mathoffstickerbook.com/sync/ehaftEyG7fPRFQE0ZJNG

This script contains the main routine that solves the puzzle_solver puzzle"""
from puzzle_solver.puzzle.solver import solve_stickerbook_puzzle

if __name__ == "__main__":
    with open('puzzle_solver/inputs/puzzle_str.txt', 'r') as reader:
        puzzle_str = reader.read()

    print(solve_stickerbook_puzzle(puzzle_str))    
