""" Problem 20
Start: Sep/14/2021 7:25pm
Finished: Sep/14/2021 7:25pm
"""

from math import factorial

def compute(n):
    n_factorial = factorial(n)
    digits = list(map(int,str(n_factorial)))
    return sum(digits)

n = 100
print(f"Sum of Digits of {n}! Is: {compute(n)}")