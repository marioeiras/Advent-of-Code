import sys


blocks = [block.splitlines() for block in sys.stdin.read().split('\n\n')]

machines = []
for block_a, block_b, block_p in blocks:
    button_a = [int(c[2:]) for c in block_a[10:].split(', ')]
    button_b = [int(c[2:]) for c in block_b[10:].split(', ')]
    prize = [int(c[2:]) for c in block_p[7:].split(', ')]
    machines.append((button_a, button_b, prize))

# Assumptions: The vectors of button A and button B are linearly independent i.e if there is a way to get the prize it is unique.
def cost(button_a, button_b, prize):
    xa, ya = button_a
    xb, yb = button_b
    xp, yp = prize
    a = (yp * xb - xp * yb) // (ya * xb - xa * yb)
    b = (yp * xa - xp * ya) // (yb * xa - xb * ya)
    if a * xa + b * xb == xp and a * ya + b *  yb == yp:
        return 3 * a + b
    return 0

print(sum(cost(button_a, button_b, prize) for button_a, button_b, prize in machines))
print(sum(cost(button_a, button_b, (10000000000000 + prize_x, 10000000000000 + prize_y)) for button_a, button_b, (prize_x, prize_y) in machines))
