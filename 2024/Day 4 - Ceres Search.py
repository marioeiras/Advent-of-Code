import sys


matrix = sys.stdin.read().splitlines()

def match_xmas(r, c, dr, dc):
    word = 'XMAS'
    for i in range(len(word)):
        if not (0 <= r + i * dr < len(matrix)) or not (0 <= c + i * dc < len(matrix[0])) or matrix[r + i * dr][c + i * dc] != word[i]:
                return False
    return True

directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
print(sum(match_xmas(r, c, dr, dc) for r in range(len(matrix)) for c in range(len(matrix[0])) for (dr, dc) in directions))

def match_x_mas(r, c):
    return (0 < r < len(matrix) - 1 and 0 < c < len(matrix[0]) - 1 and
        matrix[r][c] == 'A' and
        (matrix[r - 1][c - 1] == 'M' and matrix[r + 1][c + 1] == 'S' or matrix[r - 1][c - 1] == 'S' and matrix[r + 1][c + 1] == 'M') and
        (matrix[r - 1][c + 1] == 'M' and matrix[r + 1][c - 1] == 'S' or matrix[r - 1][c + 1] == 'S' and matrix[r + 1][c - 1] == 'M'))

print(sum(match_x_mas(r, c) for r in range(len(matrix)) for c in range(len(matrix[0]))))
