n = int(input("Enter number of queens: "))

board = [[0] * n for _ in range(n)]

def is_attack(i, j):
    # Check row and column
    for k in range(n):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # Check diagonals
    for k in range(n):
        for l in range(n):
            if (k + l == i + j or k - l == i - j) and board[k][l] == 1:
                return True
    return False

def N_queen(row):
    if row == n:
        return True
    for j in range(n):
        if not is_attack(row, j):
            board[row][j] = 1
            if N_queen(row + 1):
                return True
            board[row][j] = 0
    return False

if N_queen(0):
    for i in board:
        print(i)
else:
    print("No solution exists")