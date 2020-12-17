"""Aim: automate the process of solving puzzles Scroggs posts in Puzzle Village from his stickerbook webpage, i.e. http://mathoffstickerbook.com/sync/ehaftEyG7fPRFQE0ZJNG

Thos script contains essential packages and functions the solver relies on."""
import itertools
import numpy as np

def word_fn(
    a: int, 
    word: str, 
    b: int
):
    """
    Perform one of the four key operation according to which key word was entered
    a: int. First number in expression
    word: str. Must be 'plus', 'minus', 'times', 'divide'
    b: int. Second number in expression
    """
    if word == 'plus':
        return a + b
    elif word == 'minus':
        return a - b
    elif word == 'times':
        return a * b
    elif word == 'divide':
        return a / b

def LHS(
    a: int,
    op1: str, 
    b : int,
    op2: str,
    c: float
):
    """
    E.g. LHS(a, 'plus', b, 'times', c) does
     (a + b) * c
     params:
     a: int. First number in equation
     op1: str. Must be 'plus', 'minus', 'times', 'divide'
     b : int. Second number in equation
     op2: str. Must be 'plus', 'minus', 'times', 'divide'
     c: float. Third number in equation
     return: int
     """
    step_1 = word_fn(a, op1, b)
    step_2 = word_fn(step_1, op2, c)
    return step_2

def arr_to_str(solution):
    sol_string = '\n'.join(
        ' '.join(
            [str(num) 
             for num 
             in row]) 
        for row 
        in solution
    )
    return sol_string
    
    
def solve_puzzle(puzzle):
    perms = itertools.permutations(range(1,10), r=None)

    for item in perms:
        a, b, c, d, e, f, g, h, i = item

        row1 = LHS(a, puzzle[0][0], b, puzzle[0][1], c) == puzzle[0][2]
        row2 = LHS(d, puzzle[1][0], e, puzzle[1][1], f) == puzzle[1][2]
        row3 = LHS(g, puzzle[2][0], h, puzzle[2][1], i) == puzzle[2][2]
        col1 = LHS(a, puzzle[3][0], d, puzzle[3][1], g) == puzzle[3][2]
        col2 = LHS(b, puzzle[4][0], e, puzzle[4][1], h) == puzzle[4][2]
        col3 = LHS(c, puzzle[5][0], f, puzzle[5][1], i) == puzzle[5][2]

        if all([row1,row2,row3,col1,col2,col3]):
            print("The solution is:")
            solution = np.array(item).reshape((3, 3))
            return arr_to_str(solution)
            break
            
def process_str(puzzle_str):
    puzzle = [
        part.split(' ') 
        for part 
        in puzzle_str.split('\n')
    ]
    
    puzzle = [
        row[:2] +[int(row[2])] 
        for row 
        in puzzle 
        if len(row) == 3
    ]
    
    return puzzle
