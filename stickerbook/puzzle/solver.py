"""Aim: automate the process of solving puzzles Scroggs posts in Puzzle Village from his stickerbook webpage, i.e. http://mathoffstickerbook.com/sync/ehaftEyG7fPRFQE0ZJNG

This script contains the main routine that solves the stickerbook puzzle"""
from stickerbook.puzzle.utils import process_str, solve_puzzle

def solve_stickerbook_puzzle(puzzle_str: str) -> str:
    processed_puzzle = process_str(puzzle_str)
    solved_puzzle = solve_puzzle(processed_puzzle)

    return solved_puzzle
