""" Problem 14
Start: Sep/12/2021 5:00pm
Finished: Sep/12/2021 5:45pm
"""

def collatz_len_gen(n):
    len = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n+1
        len += 1
    yield len

def compute(n):
    max_len = 0
    max_start = 0
    for start in range(n, 0, -1):
        seq_len = next(collatz_len_gen(start))
        if seq_len > max_len:
            max_len = seq_len
            max_start = start
    return max_start

n = 1_000_000
print(f"The Number Under {n} That Produces the Longest Chain Is: {compute(n)}")