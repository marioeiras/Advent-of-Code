import sys
from collections import defaultdict


robots = []
for i, line in enumerate(sys.stdin.read().splitlines()):
    p, v = line.split()
    x, y = p[2:].split(',')
    vx, vy = v[2:].split(',')
    robots.append((int(x), int(y), int(vx), int(vy)))

def positions_after(seconds):
    positions = defaultdict(int)
    for robot in robots:
        x, y, vx, vy = robot
        nx, ny = (x + vx * seconds) % 101, (y + vy * seconds) % 103
        positions[(nx, ny)] += 1
    return positions

positions = positions_after(100)
count1 = sum(count for (x, y), count in positions.items() if x < 101 // 2 and y < 103 // 2)
count2 = sum(count for (x, y), count in positions.items() if x < 101 // 2 and y > 103 // 2)
count3 = sum(count for (x, y), count in positions.items() if x > 101 // 2 and y < 103 // 2)
count4 = sum(count for (x, y), count in positions.items() if x > 101 // 2 and y > 103 // 2)
print(count1 * count2 * count3 * count4)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def blob_size(positions):
    max_size = 0
    not_visited = set(positions)
    while not_visited:
        x, y = not_visited.pop()
        stack = [(x, y)]
        visited = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in directions:
                if (x + dx, y + dy) in positions:
                    stack.append((x + dx, y + dy))
        max_size = max(max_size, len(visited))
    return max_size

seconds = 0
while blob_size(positions_after(seconds)) < 20:
    seconds += 1

print(seconds)
