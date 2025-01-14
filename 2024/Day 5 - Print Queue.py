import sys


orderring_text, update_text = sys.stdin.read().split('\n\n')
ordering = [[int(n) for n in line.split('|')] for line in orderring_text.splitlines()]
updates = [[int(n) for n in line.split(',')] for line in update_text.splitlines()]

orderings = {}
for a, b in ordering:
    if a not in orderings:
        orderings[a] = set()
    orderings[a].add(b)

def correct(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] in orderings:
                if update[i] in orderings[update[j]]:
                    return 0
    return update[len(update) // 2]

print(sum(correct(update) for update in updates))

def correct_order(update):
    for i in range(len(update)):
        j = i + 1
        while j < len(update):
            if update[j] in orderings and update[i] in orderings[update[j]]:
                update = update[: i] + [update[j]] + update[i: j] + update[j + 1:]
            else:
                j += 1
    return update[len(update) // 2]

print(sum(correct_order(update) for update in updates if not correct(update)))
