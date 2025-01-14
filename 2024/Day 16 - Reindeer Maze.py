import sys
from collections import defaultdict
from heapq import heappush, heappop


map = [line for line in sys.stdin.read().splitlines()]

for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == 'S':
            sr, sc = r, c
        if map[r][c] == 'E':
            er, ec = r, c

heap = [(0, sr, sc, 0, 1, sr, sc, 0, 1)]
visited = {}
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
previous = defaultdict(list)
while heap:
    score, r, c, cdr, cdc, pr, pc, pdr, pdc = heappop(heap)
    if (r, c, cdr, cdc) not in visited or (r, c, cdr, cdc) in visited and visited[(r, c, cdr, cdc)] == score:
        previous[(r, c, cdr, cdc)].append((pr, pc, pdr, pdc))
    if (r, c, cdr, cdc) in visited:
        continue
    visited[(r, c, cdr, cdc)] = score
    if (r, c) == (er, ec):
        print(score)
        break
    for dr, dc in directions:
        if (dr, dc) != (cdr, cdc):
            heappush(heap, (score + 1000, r, c, dr, dc, r, c, cdr, cdc))
        elif 0 <= r + dr < len(map) and 0 <= c + dc < len(map[0]) and map[r + dr][c + dc] != '#':
            heappush(heap, (score + 1, r + dr, c + dc, dr, dc, r, c, cdr, cdc))

stack = [(r, c, cdr, cdc)]
visited = set()
while stack:
    r, c, dr, dc = stack.pop()
    visited.add((r, c))
    if (r, c) != (sr, sc):
        stack.extend(previous[(r, c, dr, dc)])

print(len(visited))
