import sys
from collections import deque
from functools import cache


codes = sys.stdin.read().splitlines()

directional_adjacency = {'A': [('^', '<'), ('>', 'v')], '^': [('A', '>'), ('v', 'v')], '<': [('v', '>')], 'v': [('<', '<'), ('^', '^'), ('>', '>')], '>': [('A', '^'), ('v', '<')]}
numerical_adjacency = {'A': [('0', '<'), ('3', '^')], '0': [('A', '>'), ('2', '^')], '1': [('2', '>'), ('4', '^')], '2': [('0', 'v'), ('1', '<'), ('3', '>'), ('5', '^')], '3': [('A', 'v'), ('2', '<'), ('6', '^')], '4': [('1', 'v'), ('5', '>'), ('7', '^')], '5': [('2', 'v'), ('4', '<'), ('6', '>'), ('8', '^')], '6': [('3', 'v'), ('5', '<'), ('9', '^')], '7': [('4', 'v'), ('8', '>')], '8': [('5', 'v'), ('7', '<'), ('9', '>')], '9': [('6', 'v'), ('8', '<')]}

def find_paths(source, target, keypad_adjacency):
    queue = deque([(source, '')])
    shortest = 0
    while queue:
        button, path = queue.popleft()
        if button == target:
            if not shortest or len(path) == shortest:
                shortest = len(path)
                yield path + 'A'
            continue
        if  shortest and len(path) > shortest:
            continue
        for adjacent, direction in keypad_adjacency[button]:
            queue.append((adjacent, path + direction))

def find_paths_numerical(source, target):
    return list(find_paths(source, target, numerical_adjacency))

def find_paths_directional(source, target):
    return list(find_paths(source, target, directional_adjacency))

def least_presses(code, depth, find_paths_keypad):
    if not depth:
        return len(code)
    prev_button = 'A'
    total_presses = 0
    for button in code:
        min_presses = sys.maxsize
        for path in find_paths_keypad(prev_button, button):
            presses = least_presses_directional(path, depth - 1)
            min_presses = min(presses, min_presses)
        total_presses += min_presses
        prev_button = button
    return total_presses

@cache
def least_presses_directional(code, depth):
    return least_presses(code, depth, find_paths_directional)

def least_presses_numerical(code, depth):
    return least_presses(code, depth, find_paths_numerical)

print(sum(least_presses_numerical(code, 3) * int(code[:-1]) for code in codes))
print(sum(least_presses_numerical(code, 26) * int(code[:-1]) for code in codes))
