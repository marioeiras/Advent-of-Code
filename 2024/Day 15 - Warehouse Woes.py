import sys


warehouse_part, instructions_part = sys.stdin.read().split('\n\n')
warehouse = [[c for c in line] for line in warehouse_part.splitlines()]
directions = {'v': (1, 0), '>': (0, 1), '^': (-1, 0), '<': (0, -1)}
instructions = [i for i in instructions_part if i in directions]

box_positions = {(r, c) for r in range(len(warehouse)) for c in range(len(warehouse[0])) if warehouse[r][c] == 'O'}
robot_position = [(r, c) for r in range(len(warehouse)) for c in range(len(warehouse[0])) if warehouse[r][c] == '@'][0]

r, c = robot_position
for instruction in instructions:
    dr, dc = directions[instruction]
    i = 1
    while (r + i * dr, c + i * dc) in box_positions:
        i += 1
    if warehouse[r + i * dr][c + i * dc] != '#':
        if (r + dr, c + dc) in box_positions:
            box_positions.remove((r + dr, c + dc))
            box_positions.add((r + i * dr, c + i * dc))
        r, c = r + dr, c + dc

print(sum(100 * r + c for r, c in box_positions))

replacement = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
warehouse = [''.join(replacement[c] for c in row) for row in warehouse]
box_positions = {(r, c) for r in range(len(warehouse)) for c in range(len(warehouse[0])) if warehouse[r][c] == '['}
robot_position = [(r, c) for r in range(len(warehouse)) for c in range(len(warehouse[0])) if warehouse[r][c] == '@'][0]

r, c = robot_position
for instruction in instructions:
    dr, dc = directions[instruction]
    stack = [(r + dr, c + dc)]
    boxes_to_push = set()
    while stack:
        pr, pc = stack.pop()
        if warehouse[pr][pc] == '#':
            break
        elif (pr, pc) in box_positions and (pr, pc) not in boxes_to_push:
            boxes_to_push.add((pr, pc))
            stack.append((pr + dr, pc + dc + 1))
            if instruction != '>':
                stack.append((pr + dr, pc + dc))
        elif (pr, pc - 1) in box_positions and (pr, pc - 1) not in boxes_to_push:
            boxes_to_push.add((pr, pc - 1))
            stack.append((pr + dr, pc + dc - 1))
            if instruction != '<':
                stack.append((pr + dr, pc + dc))
    if warehouse[pr][pc] != '#':
        for br, bc in boxes_to_push:
            box_positions.remove((br, bc))
        for br, bc in boxes_to_push:
            box_positions.add((br + dr, bc + dc))
        r, c = r + dr, c + dc

print(sum(100 * r + c for r, c in box_positions))
