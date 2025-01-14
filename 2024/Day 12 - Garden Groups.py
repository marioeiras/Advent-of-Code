import sys


garden = [line for line in sys.stdin.read().splitlines()]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def plot_measurements(r, c):
    area = 0
    perimeter = 0
    stack = [(r, c)]
    side_count = 0
    sides = set()
    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        area += 1
        for dr, dc in directions:
            if 0 <= r + dr < len(garden) and 0 <= c + dc < len(garden[0]) and garden[r + dr][c + dc] == garden[r][c]:
                stack.append((r + dr, c + dc))
            else:
                perimeter += 1
                if (r, c, r + dr, c + dc) not in sides:
                    side_count += 1
                    k = 0
                    while 0 <= r - k * dc < len(garden) and 0 <= c + k * dr < len(garden[0]) and garden[r - k * dc][c + k * dr] == garden[r][c] and not (0 <= r - k * dc + dr < len(garden) and 0 <= c + k * dr + dc < len(garden[0]) and garden[r - k * dc + dr][c + k * dr + dc] == garden[r][c]):
                        sides.add((r - k * dc, c + k * dr, r - k * dc + dr, c + k * dr + dc))
                        k += 1
                    k = -1
                    while 0 <= r - k * dc < len(garden) and 0 <= c + k * dr < len(garden[0]) and garden[r - k * dc][c + k * dr] == garden[r][c] and not (0 <= r - k * dc + dr < len(garden) and 0 <= c + k * dr + dc < len(garden[0]) and garden[r - k * dc + dr][c + k * dr + dc] == garden[r][c]):
                        sides.add((r - k * dc, c + k * dr, r - k * dc + dr, c + k * dr + dc))
                        k -= 1
    return area, perimeter, side_count

price, price2 = 0, 0
visited = set()
for r in range(len(garden)):
    for c in range(len(garden[0])):
        if (r, c) in visited:
            continue
        stack = [(r, c)]
        area, perimeter, side_count = plot_measurements(r, c)
        price += area * perimeter
        price2 += area * side_count

print(price)
print(price2)
