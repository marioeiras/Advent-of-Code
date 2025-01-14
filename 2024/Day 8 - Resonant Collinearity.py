import sys


map = sys.stdin.read().splitlines()

antennas = {}
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] != '.':
            if map[r][c] not in antennas:
                antennas[map[r][c]] = []
            antennas[map[r][c]].append((r, c))

# Assumptions: for any two antennas of the same frequency A and B, the vector A - B = (dr, dc) does not contain any integer points other than A and B (i.e. gcd(dr, dc) = 1).
antinodes = set()
antinodes2 = set()
for frequency in antennas:
    locations = antennas[frequency]
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            ri, ci = locations[i]
            rj, cj = locations[j]
            dr, dc = rj - ri, cj - ci
            if 0 <= ri - dr < len(map) and 0 <= ci - dc < len(map[0]):
                antinodes.add((ri - dr, ci - dc))
            if 0 <= rj + dr < len(map) and 0 <= cj + dc < len(map[0]):
                antinodes.add((rj + dr, cj + dc))
            begin = -(ri // dr)
            end = (len(map) - ri) // dr + 1
            for k in range(begin, end):
                if 0 <= ri + k * dr < len(map) and 0 <= ci + k * dc < len(map[0]):
                    antinodes2.add((ri + k * dr, ci + k * dc))

print(len(antinodes))
print(len(antinodes2))
