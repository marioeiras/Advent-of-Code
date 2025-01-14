import sys
import re


text = sys.stdin.read()

pattern = re.compile('mul\(([0-9]+),([0-9]+)\)')
print(sum(int(match[0]) * int(match[1]) for match in pattern.findall(text)))

result = 0
for part in text.split('do()'):
    do = part.split('don\'t()')[0]
    result += sum(int(match[0]) * int(match[1]) for match in pattern.findall(do))

print(result)
