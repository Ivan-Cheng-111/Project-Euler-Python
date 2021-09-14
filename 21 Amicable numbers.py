""" Problem 21
Start: Sep/14/2021 7:30pm
Finished: Sep/14/2021 7:45pm
"""
from math import isqrt

def sum_divisors(n):
	return sum(i for i in range(1, n) if n % i == 0)

def compute(n):
    # d(n) be defined as the sum of divisors of n
    # if d(a)=b, d(b)=a, a≠b, then a and b are amicable numbers
    amicable_numbers = []

    for a in range(1,n):
        b = sum_divisors(a)
        # check if a=b and for duplicates
        if a == b or a in amicable_numbers or b in amicable_numbers:
            continue
        if sum_divisors(b) == a:
            amicable_numbers.append(a)
            amicable_numbers.append(b)   
    return sum(amicable_numbers)

n = 10_000
print(f"The Sum of All Amicable Numbers Under {n} Is: {compute(n)}")