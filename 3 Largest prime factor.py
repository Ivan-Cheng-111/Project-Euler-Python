""" Problem 3
Start: Sep/09/2021 2:40pm
Finished: Sep/09/2021 6:20pm
"""

from math import isqrt

def compute(num) -> int:
    # base cases, 1 and lower is not prime, 2 and 3 is prime
    if num < 2:
        return 0
    if num <= 3:
        return num
    
    factor = 1
    # if num is even, factor out 2 until number is odd
    while num % 2 == 0:
        factor = 2
        num //= 2
    
    # two optimizations
    # i jumps from 3 by 2 because only odd numbers will be factors
    # i stop at sqrt(num) because factors cannot be larger than it 
    for i in range(3, isqrt(num)+1,2):
        # check if divisible i, divide by i until not divisible
        while num % i == 0:
            factor = i
            num //= i
        # if num is 1, largest factor is found
        if num < 2:
            return factor
    # if no factors found, the number itself is the only factor
    return num

n = 600851475143
print(f"Largest Prime Factor of {n} Is: {compute(n)}")