""" Problem 10
Start: Sep/10/2021 9:10pm
Finished: Sep/10/2021 9:45pm
"""

from itertools import repeat
from math import isqrt

# naive implementation
def compute3(n):
	# base cases, 1 and lower has no prime, 2 and lower prime sum is 2
	if n < 2:
		return 0
	if n == 2:
		return n
    
	sum = 2
    # start from 3 skip by 2 (skip even numbers)
	for i in range(3,n+1,2):
        # sqrt(i) is the largest possible factor
		for j in range(3,isqrt(i)+1,2):
			if i % j == 0:
				break
		else:
			sum += i
	return sum

# sieve of eratosthenes
def compute2(n):
    # base case 1 and lower has no prime
    if n < 2:
        return 0
    
    # make boolen list sized n, initalized as True
    is_prime = [True] * n
    # mark out 0 and 1 as False
    is_prime[0] = is_prime[1] = False

    # mark out all even numbers 4 and above
    if n % 2 == 0:
        for i in range(2*2, n, 2):
            is_prime[i] = False
    
    # if True, mark out its multiples as False
    for i in range(3, isqrt(n)+1,2):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False
    
    # return sum of primes
    return sum(i for i in range(n) if is_prime[i])

# loop optimized sieve of eratosthenes
def compute(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    if n % 2 == 0:
        is_prime[2*2::2] = repeat(False, len(range(2*2, n, 2)))
    
    for i in range(3,isqrt(n)+1,2):
        if is_prime[i]:
            is_prime[i*i::i] = repeat(False, len(range(i*i, n, i)))
    
    return sum(i for i in range(n) if is_prime[i])

n = 2_000_000
print(f"Sum of All the Primes Below {n:_} Is: {compute(n)}")