""" Problem 12
Start: Sep/11/2021 8:10pm
Finished: Sep/12/2021 2:45pm
"""

from math import isqrt
from timeit import default_timer as time
import itertools

def num_divisors(n):
	end = isqrt(n)
	result = sum(2 for i in range(1, end + 1) if n % i == 0)
	if end*end == n:
		result -= 1
	return result

def compute(n):
	tri_num = 0
	for i in itertools.count(1):
		tri_num += i
		if num_divisors(tri_num) > n:
			return tri_num

n = 500
val = compute(n)
print(f"Value of the First Triangle Number With Over {n} Divisors Is: {compute(n)}")