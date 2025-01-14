import sys


reports = [list(map(int, line)) for line in [line.split() for line in sys.stdin.read().splitlines()]]

def safe(report):
    prev = report[0]
    inc = report[1] > prev
    for i in range(1, len(report)):
        if inc and report[i] <= prev or not inc and report[i] >= prev or abs(prev - report[i]) > 3:
            return False
        prev = report[i]
    return True

print(sum(safe(report) for report in reports))

def safe_tolerate(report):
    for j in range(len(report)):
        if safe(report[: j] + report[j + 1:]):
            return True
    return False

print(sum(safe_tolerate(report) for report in reports))
