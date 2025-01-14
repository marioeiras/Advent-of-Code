import sys
from collections import deque


track = sys.stdin.read().splitlines()

for r in range(len(track)):
    for c in range(len(track[0])):
        if track[r][c] == 'S':
            sr, sc = r, c
        elif track[r][c] == 'E':
            er, ec = r, c

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def reachable_times(start):
    queue = deque([(0, *start)])
    known_times = {}
    while queue:
        time, r, c = queue.popleft()
        if (r, c) in known_times:
            continue
        known_times[(r, c)] = time
        for dr, dc in directions:
            if 0 <= r + dr < len(track) and 0 <= c + dc < len(track[0]) and track[r + dr][c + dc] != '#':
                queue.append((time + 1, r + dr, c + dc))
    return known_times

def count_cheats(start, time_to_finish, cutoff_time, cheating_time):
    count = 0
    queue = deque([(0, *start)])
    visited = set()
    while queue:
        time, r, c = queue.popleft()
        if (r, c) in visited or time > cutoff_time:
            continue
        visited.add((r, c))
        for dr, dc in directions:
            if 0 <= r + dr < len(track) and 0 <= c + dc < len(track[0]) and track[r + dr][c + dc] != '#':
                queue.append((time + 1, r + dr, c + dc))
        for dr in range(-cheating_time, cheating_time + 1):
            for dc in range(-cheating_time + abs(dr), cheating_time - abs(dr) + 1):
                if (r + dr, c + dc) in time_to_finish and time + time_to_finish[(r + dr, c + dc)] + abs(dr) + abs(dc) <= cutoff_time:
                    count += 1
    return count

time_to_finish = reachable_times((er, ec))
honest_time = time_to_finish[(sr, sc)]

print(count_cheats((sr, sc), time_to_finish, honest_time - 100, 2))
print(count_cheats((sr, sc), time_to_finish, honest_time - 100, 20))
