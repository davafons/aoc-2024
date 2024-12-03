import random

n = 100000
output_file = 'input_big.txt'
with open(output_file, 'w') as f:
    for _ in range(n):
        f.write(f"{random.randint(0, 99)} {random.randint(0, 99)}\n")

print("Generated")