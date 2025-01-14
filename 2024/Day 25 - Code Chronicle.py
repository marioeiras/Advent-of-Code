import sys


schematics = [part.split() for part in sys.stdin.read().split('\n\n')]

locks = []
keys = []
for schematic in schematics:
    if schematic[0][0] == '#':
        heights = tuple(max(r for r in range(7) if schematic[r][c] == '#') for c in range(5))
        locks.append(heights)
    else:
        heights = tuple(min(r for r in range(7) if schematic[r][c] == '#') for c in range(5))
        keys.append(heights)

print(sum(all(key[c] > lock[c] for c in range(5)) for lock in locks for key in keys))
