import sys
from collections import Counter


pairs = [(int(left), int(right)) for left, right in [line.split() for line in sys.stdin.read().splitlines()]]
left, right = zip(*pairs)

print(sum(abs(l - r) for l, r in zip(sorted(left), sorted(right))))

counter = Counter(right)
print(sum(l * counter[l] for l in left))
