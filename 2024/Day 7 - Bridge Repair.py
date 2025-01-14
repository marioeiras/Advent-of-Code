import sys


equations = [(int(left), [int(r) for r in right.split()]) for left, right in [line.split(':') for line in sys.stdin.read().splitlines()]]

def valid(test, numbers):
    for i in range(2 ** (len(numbers) - 1)):
        result = numbers[0]
        for j in range(1, len(numbers)):
            if i & 1:
                result += numbers[j]
            else:
                result *= numbers[j]
            i >>= 1
        if result == test:
            return True
    return False

print(sum(result for result, numbers in equations if valid(result, numbers)))

def valid(test, numbers):
    for i in range(3 ** (len(numbers) - 1)):
        result = numbers[0]
        for j in range(1, len(numbers)):
            if i % 3 == 0:
                result += numbers[j]
            elif i % 3 == 1:
                result *= numbers[j]
            else:
                n = numbers[j]
                while n:
                    n //= 10
                    result *= 10
                result += numbers[j]
            i //= 3
        if result == test:
            return True
    return False

print(sum(result for result, numbers in equations if valid(result, numbers)))
