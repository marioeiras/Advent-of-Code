import sys


lines = sys.stdin.read().splitlines()
ra = int(lines[0][12:])
rb = int(lines[1][12:])
rc = int(lines[2][12:])
instructions = [int(n) for n in lines[4][9:].split(',')]

def run(instructions, ra):
    def combo(operand):
        if operand == 4:
            return ra
        elif operand == 5:
            return rb
        elif operand == 6:
            return rc
        return operand
    pointer = 0
    while pointer < len(instructions):
        instruction = instructions[pointer]
        operand = instructions[pointer + 1]
        pointer += 2
        if instruction == 0:
            ra = ra >> combo(operand)
        elif instruction == 1:
            rb = rb ^ operand
        elif instruction == 2:
            rb = combo(operand) % 8
        elif instruction == 3:
            pointer = operand if ra else pointer
        elif instruction == 4:
            rb = rb ^ rc
        elif instruction == 5:
            yield combo(operand) % 8
        elif instruction == 6:
            rb = ra >> combo(operand)
        elif instruction == 7:
            rc = ra >> combo(operand)

print(','.join([str(n) for n in run(instructions, ra)]))

def find_ra(instructions, expected_output, known_length = 0, known_ra = 0):
    if known_length == len(expected_output):
        return known_ra
    known_length += 1
    for triplet in range(8):
        ra = known_ra * 8 + triplet
        if list(run(instructions, ra)) == expected_output[-known_length:]:
            found_ra = find_ra(instructions, expected_output, known_length, ra)
            if found_ra != None:
                return found_ra
    return None

print(find_ra(instructions, instructions))
