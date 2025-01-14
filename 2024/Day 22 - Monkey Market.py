import sys
from collections import defaultdict


numbers = [int(n) for n in sys.stdin.read().split()]

def generate_secrets(secret, iterations):
    yield secret
    for _ in range(iterations):
        secret ^= secret * 64 % 16777216 
        secret ^= secret // 32
        secret ^= secret * 2048 % 16777216
        yield secret

secret_sum = 0
counter = defaultdict(int)
for number in numbers:
    secrets = list(generate_secrets(number, 2000))
    diffs = [secrets[i] % 10 - secrets[i - 1] % 10 for i in range(1, len(secrets))]
    secret_sum += secrets[-1]
    visited = set()
    for i in range(3, len(diffs)):
        sequence = tuple(diffs[i - 3: i + 1])
        if (sequence in visited):
            continue
        counter[sequence] += secrets[i] % 10
        visited.add(sequence)

print(secret_sum)
print(max(counter.values()))
