"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List, Tuple, Union


def check(line: Union[List, Tuple]) -> str:
    """Check the state of the line (column, row or diagonal) of
    tic tac toe 3x3 board.

    Args:
        line: column, row or diagonal of the board.

    Returns:
        "x wins!" if line consist of 3 x'es,
        "o wins!" if line consist of 3 o's,
        "maybe unfinished" if '-' in line,
        "maybe draw" otherwise.

    >>> check(['x', 'x', 'x'])
    'x wins!'

    >>> check(['o', 'o', 'o'])
    'o wins!'

    >>> check(['x', 'o', '-'])
    'maybe unfinished'

    >>> check(['x', 'o', 'x'])
    'maybe draw'
    """
    if line.count("x") == 3:
        return "x wins!"
    if line.count("o") == 3:
        return "o wins!"
    if "-" in line:
        return "maybe unfinished"
    return "maybe draw"


def tic_tac_toe_checker(board: List[List]) -> str:
    """Check if there is a winner in tic tac toe game.

    Args:
        board: 3x3 board filled with "x", "o" or "-".

    Returns:
        "x wins!" if there is "x" winner,
        "o wins!" if there is "o" winner,
        "draw!" if there is a draw,
        "unfinished!" if the board is unfinished.

    >>> tic_tac_toe_checker([['-', '-', 'o'], \
                             ['-', 'o', 'o'], \
                             ['x', 'x', 'x']])
    'x wins!'

    >>> tic_tac_toe_checker([['x', 'x', 'o'], \
                             ['x', 'o', '-'], \
                             ['o', '-', '-']])
    'o wins!'

    >>> tic_tac_toe_checker([['-', '-', 'o'], \
                             ['-', 'x', 'o'], \
                             ['x', 'o', 'x']])
    'unfinished!'

    >>> tic_tac_toe_checker([['o', 'x', 'x'], \
                             ['x', 'x', 'o'], \
                             ['o', 'o', 'x']])
    'draw!'
    """
    options = []
    board_transposed = zip(*board)
    for row, column in zip(board, board_transposed):
        options.extend([check(row), check(column)])
    main_diag = [board[i][i] for i in range(3)]
    minor_diag = [board[i][2 - i] for i in range(3)]
    options.extend([check(main_diag), check(minor_diag)])

    if "x wins!" in options:
        return "x wins!"
    if "o wins!" in options:
        return "o wins!"
    if "maybe unfinished" in options:
        return "unfinished!"
    return "draw!"
