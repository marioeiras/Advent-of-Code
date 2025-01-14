import sys
from collections import deque


obstacles = [tuple([int(n) for n in line.split(',')]) for line in sys.stdin.read().splitlines()]

def min_steps(obstacles):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(0, 0, 0)])
    visited = set()
    while queue:
        steps, r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if (r, c) == (70, 70):
            return steps
        for dr, dc in directions:
            if 0 <= r + dr < 71 and 0 <= c + dc < 71 and (r + dr, c + dc) not in obstacles:
                queue.append((steps + 1, r + dr, c + dc))

print(min_steps(obstacles[:1024]))

low = 1024
high = len(obstacles)
while high - low > 1:
    mid = (high + low) // 2
    if min_steps(set(obstacles[:mid])):
        low = mid
    else:
        high = mid

print(f'{obstacles[low][0]},{obstacles[low][1]}')
