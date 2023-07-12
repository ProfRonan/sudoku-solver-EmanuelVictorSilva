def solve_sudoku(board):
    if not is_valid(board):
        return None
    
    if is_complete(board):
        return board
    
    row, col = find_empty_cell(board)
    
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return board
            
            board[row][col] = 0
    
    return None


def is_valid(board):
    for i in range(9):
        if not is_valid_row(board, i) or not is_valid_column(board, i) or not is_valid_subgrid(board, i):
            return False
    return True


def is_valid_row(board, row):
    nums = set()
    for num in board[row]:
        if num != 0:
            if num in nums:
                return False
            nums.add(num)
    return True


def is_valid_column(board, col):
    nums = set()
    for i in range(9):
        num = board[i][col]
        if num != 0:
            if num in nums:
                return False
            nums.add(num)
    return True


def is_valid_subgrid(board, subgrid):
    start_row = (subgrid // 3) * 3
    start_col = (subgrid % 3) * 3
    nums = set()
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            num = board[i][j]
            if num != 0:
                if num in nums:
                    return False
                nums.add(num)
    return True


def is_valid_move(board, row, col, num):
    return is_valid_row(board, row) and is_valid_column(board, col) and is_valid_subgrid(
        board, (row // 3) * 3 + col // 3)


def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None
