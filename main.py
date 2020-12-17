"""Aim: automate the process of solving puzzles Scroggs posts in Puzzle Village from his stickerbook webpage, i.e. http://mathoffstickerbook.com/sync/ehaftEyG7fPRFQE0ZJNG

This script contains the main routine that solves the stickerbook puzzle"""
from stickerbook.puzzle.solver import solve_stickerbook_puzzle

if __name__ == "__main__":
    with open('./stickerbook/inputs/puzzle_str.txt','r') as reader:
        puzzle_str = reader.read()

    print(solve_stickerbook_puzzle(puzzle_str))    
