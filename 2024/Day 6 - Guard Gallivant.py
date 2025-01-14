import sys


map = sys.stdin.read().splitlines()

def is_loop(r, c, dr, dc, obstacle, previous):
    directions = set(previous)
    while 0 <= r < len(map) and 0 <= c < len(map[0]):
        if (r, c, dr, dc) in directions:
            return True
        directions.add((r, c, dr, dc))
        if (r + dr, c + dc) == obstacle or 0 <= r + dr < len(map) and 0 <= c + dc < len(map[0]) and map[r + dr][c + dc] == '#':
            dr, dc = dc, -dr
        else:
            r += dr
            c += dc
    return False

r, c = [(r, c) for r in range(len(map)) for c in range(len(map[0])) if map[r][c] == '^'][0]
dr, dc = (-1, 0)
visited = set()
directions = set()
obstacles = set()
while 0 <= r < len(map) and 0 <= c < len(map[0]):
    directions.add((r, c, dr, dc))
    if 0 <= r + dr < len(map) and 0 <= c + dc < len(map[0]) and map[r + dr][c + dc] == '#':
        dr, dc = dc, -dr
    else:
        visited.add((r, c))
        if (r + dr, c + dc) not in visited and is_loop(r, c, dc, -dr, (r + dr, c + dc), directions):
            obstacles.add((r + dr, c + dc))
        r += dr
        c += dc

print(len(visited))
print(len(obstacles))
