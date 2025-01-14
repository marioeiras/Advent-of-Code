import sys
from collections import defaultdict


input_part, instructions_part = sys.stdin.read().split('\n\n')

input = defaultdict(int)
for part in input_part.splitlines():
    input[str(part[0: 3])] = int(part[5:])
pp = False
instructions_input = dict()
instructions_output = dict()
values = set(input)
for inst in instructions_part.splitlines():
    part = inst.split()
    instructions_input[(part[0], part[2])] = (part[1], part[0], part[2], part[4])
    instructions_output[part[4]] = (part[1], part[0], part[2], part[4])
    values.add(part[0])
    values.add(part[2])
    values.add(part[4])


def compute(value):
    if value in input:
        return input[value]
    i, l, r, o = instructions_output[value]
    #l, r = sorted([l, r])
    if pp:
        print(l, r, i, o)
    if i == 'AND':
        return compute(l) & compute(r)
    elif i == 'OR':
        return compute(l) | compute(r)
    elif i == 'XOR':
        return compute(l) ^ compute(r)
    
#index = 0
def compute_z():
    z = 0
    for index in range(46):
        #print('===z' + f'{index:02}')
        z += 2 ** index * compute('z' + f'{index:02}')
    return z

z = compute_z()

def compute_y():
    y = 0
    for index in range(45):
        #print('===z' + f'{index:02}')
        y += 2 ** index * compute('y' + f'{index:02}')
    return y

y = compute_y()

def compute_x():
    x = 0
    for index in range(45):
        #print('===z' + f'{index:02}')
        x += 2 ** index * compute('x' + f'{index:02}')
    return x

x = compute_x()




def count_diffs(x, y, z):
    d = (x + y) ^ z
    print(f'{x:b}')
    print(f'{y:b}')
    print(f'{z:b}')
    print(f'{x + y:b}')
    print(f'{d:b}')
    for i in range(46):
        if (d & (1 << i)) != 0:
            print(i)
    return sum((d & (1 << i)) != 0 for i in range(46))

print('1', count_diffs(x, y, z))

pp = True
compute('z37')

# TODO: Implement automatic solution. Fix the input file that is already 'solved' for second part.
print(','.join(sorted(['mwp','btb','rdg', 'z30', 'rmj', 'z23', 'z17','cmv'])))
