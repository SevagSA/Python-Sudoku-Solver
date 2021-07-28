import numpy as np

sudoku = [[7, 8, 0, 4, 0, 0, 1, 2, 0], [6, 0, 0, 0, 7, 5, 0, 0, 9], [0, 0, 0, 6, 0, 1, 0, 7, 8],
          [0, 0, 7, 0, 4, 0, 2, 6, 0], [0, 0, 1, 0, 5, 0, 9, 3, 0], [9, 0, 4, 0, 6, 0, 0, 0, 5],
          [0, 7, 0, 3, 0, 0, 0, 1, 2], [1, 2, 0, 0, 0, 7, 4, 0, 0], [0, 4, 9, 2, 0, 6, 0, 0, 7]]


def number_is_valid(row, col, num) -> bool:
    """
    Determine if inputting the given number in the given position is valid.

    :param row: The row of the given position.
    :param col: The column of the given position.
    :param num: The given number.
    :return: True if inputting the given number in the given position is valid.
    """

    # Verify if num exists in given row
    for i in sudoku[row]:
        if i == num:
            return False

    # Verify if num exists in given column
    for i in range(len(sudoku)):
        if sudoku[i][col] == num:
            return False

    # Verify the square of the given position
    square_x = (col // 3) * 3
    square_y = (row // 3) * 3

    for i in range(square_y, square_y + 3):
        for j in range(square_x, square_x + 3):
            if sudoku[i][j] == num:
                return False

    return True


def solve() -> None:
    """
    Solve the sudoku, i.e. fill in all of the empty cells with valid numbers.

    :return: None. The function prints the solved sudoku.
    """
    for i in range(9):  # Number of rows in the sudoku
        for j in range(9):  # Number of columns in the sudoku
            if sudoku[i][j] == 0:  # If the cell is empty
                for n in range(10):  # Loop through possible numbers -> 0-9
                    if number_is_valid(i, j, n):
                        sudoku[i][j] = n  # Replace 0 with the valid number
                        solve()  # Recurse function to solve the following cell
                        # If there's no valid number for the following
                        # empty cell, replace this cell with 0 to backtrack.
                        sudoku[i][j] = 0
                return
    print(np.matrix(sudoku))


solve()
