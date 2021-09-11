""" Problem 2
Start: Sep/09/2021 12:50pm
Finished: Sep/09/2021 6:30pm
"""

def compute(max):
    # initalize first 2 fibonnaci numbers 1,1
    x = y = 1
    sum = 0
    while x < max:
        # check if x is even, add to sum
        if x % 2 == 0:
            sum += x
        # generate next fibonnaci number
        x, y = y, x+y
    yield sum

# next once because generator only yeilds sum
n = 4_000_000
print(f"Sum of All Even Fibonacci Numbers Less Than {n:_} Is: {next(compute(n))}")