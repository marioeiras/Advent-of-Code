import sys
from collections import Counter, defaultdict


numbers = [int(n) for n in sys.stdin.read().split()]

def count(iterations):
    results = Counter(numbers)
    for _ in range(iterations):
        new_results = defaultdict(int)
        for n, c in results.items():
            if n == 0:
                new_results[1] += c
            elif not len(text := str(n)) & 1:
                new_results[int(text[: len(text) // 2])] += c
                new_results[int(text[len(text) // 2:])] += c
            else:
                new_results[n * 2024] += c
        results = new_results
    return sum(c for _, c in results.items())

print(count(25))
print(count(75))
