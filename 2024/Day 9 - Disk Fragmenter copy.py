import sys
from bisect import bisect_left
from collections import deque
from itertools import accumulate


sizes = [int(n) for n in sys.stdin.read().strip()]

checksum = 0
last_index = len(sizes) - 1 if len(sizes) & 1 else len(sizes) - 2
last_size = sizes[last_index]
position = 0
for i in range(len(sizes)):
    if i > last_index:
        break
    size = sizes[i] if i < last_index else last_size
    if i & 1:
        while last_size <= size and last_index > i:
            checksum += last_index // 2 * (2 * position + last_size - 1) * last_size // 2
            position += last_size
            size -= last_size
            last_index -= 2
            last_size = sizes[last_index]
        if last_index > i:
            checksum += last_index // 2 * (2 * position + size - 1) * size // 2
            position += size
            last_size -= size
    else:
        checksum += i // 2 * (2 * position + size - 1) * size // 2
        position += size

print(checksum)

empty = {i: deque() for i in range(0, 10)}
for i in range(len(sizes)):
    if i & 1:
        for j in range(sizes[i] + 1):
            empty[j].append(i)

checksum = 0
last_index = len(sizes) - 1 if len(sizes) & 1 else len(sizes) - 2
positions = [0] + list(accumulate(sizes))
for i in range(last_index, 0, -1):
    position = positions[i]
    if i & 1:
        if empty[sizes[i]] and empty[sizes[i]][-1] == i:
            for j in range(sizes[i] + 1):
                empty[j].pop()
    else:
        if empty[sizes[i]]:
            empty_index = empty[sizes[i]][0]
            for j in range(sizes[i], sizes[empty_index] + 1):
                if j > sizes[empty_index] - sizes[i]:
                    empty[j].popleft()
            for j in range(0, sizes[i]):
                if j > sizes[empty_index] - sizes[i]:
                    del empty[j][bisect_left(empty[j], empty_index)]
            checksum += i // 2 * (2 * positions[empty_index] + sizes[i] - 1) * sizes[i] // 2
            sizes[empty_index] -= sizes[i]
            positions[empty_index] += sizes[i]
        else:
            checksum += i // 2 * (2 * positions[i] + sizes[i] - 1) * sizes[i] // 2

print(checksum)
