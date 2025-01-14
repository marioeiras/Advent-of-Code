import sys


map = [[int(n) for n in line] for line in sys.stdin.read().splitlines()]

zeros = [(r, c) for r in range(len(map)) for c in range(len(map[0])) if map[r][c] == 0]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
score = 0
score2 = 0
for zero in zeros:
    stack = [zero]
    solutions = set()
    while stack:
        r, c = stack.pop()
        if map[r][c] == 9:
            solutions.add((r, c))
            score2 += 1
            continue
        for dr, dc in directions:
            if 0 <= r + dr < len(map) and 0 <= c + dc < len(map[0]) and map[r + dr][c + dc] == map[r][c] + 1:
                stack.append((r + dr, c + dc))
    score += len(solutions)


print(score)
print(score2)
