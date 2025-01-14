import sys
from functools import cache


patterns_text, designs_text = sys.stdin.read().split('\n\n')
patterns = patterns_text.split(', ')
designs = designs_text.splitlines()

@cache
def match_count(design):
    if design == '':
        return 1
    return sum(match_count(design[len(pattern):]) for pattern in patterns if design.startswith(pattern))

print(sum(match_count(design) > 0 for design in designs))
print(sum(match_count(design) for design in designs))
