def print_sudoku(a):
    for i in range(9):
        for j in range(9):
            print(a[i][j], end = ' ')
        print()

def get_unassigned_location(a):
    for i in range(9):
        for j in range(9):
            if a[i][j] == 0:
                return i, j
    return 9, 9

def check_row(a, r, n):
    for j in range(9):
        if a[r][j] == n:
            return False
    return True

def check_column(a, c, n):
    for i in range(9):
        if a[i][c] == n:
            return False
    return True

def check_box(a, r, c, n):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if a[i][j] == n:
                return False
    return True

def is_safe(a, r, c, n):
    return check_row(a, r, n) and check_column(a, c, n) and check_box(a, r - r%3, c - c%3, n)

def solve(a):
    r, c = get_unassigned_location(a)
    if r == 9 and c == 9:
        return True
    for n in range(1, 10):
        if is_safe(a, r, c, n):
            a[r][c] = n
            if solve(a):
                return True
            a[r][c] = 0
    return False

a = [list(map(int, input().split())) for _ in range(9)]
solve(a)
print_sudoku(a)
