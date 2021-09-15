""" Problem 25
Start: Sep/15/2021 1:50am
Finished: Sep/15/2021 1:55am
"""

def compute(n):
    # initalize first 2 terms 1,1
    x = y = 1
    idx = 2
    while len(str(x)) < n:
        # generate next fibonnaci number and increase index
        x, y = y, x+y
        idx += 1
    yield idx-1

n = 1000
print(f"The Index of the First Term In the Fibonacci Sequence To Contain {n} Digits Is: {next(compute(n))}")