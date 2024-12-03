import numpy as np

l1, l2 = np.loadtxt('input.txt', unpack=True, dtype=int)

# Part one
print(f"Part one: {np.sum(np.abs(np.sort(l1) - np.sort(l2)))}")

# Part two
mem = {}
print(f"Part two: {sum(mem.setdefault(x, x * np.count_nonzero(l2 == x)) for x in l1)}")
