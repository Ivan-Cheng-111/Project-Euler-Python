""" Problem 10
Start: Sep/10/2021 9:10pm
Finished: Sep/10/2021 9:45pm
"""

from itertools import repeat
from bisect import bisect_right
from math import isqrt

# classical sieve of eratosthenes
def compute2(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    # mark out 0 and 1 as False
    is_prime[0] = is_prime[1] = False

    if n % 2 == 0:
        for i in range(2*2, n, 2):
            is_prime[i] = False
    # if True, mark out its multiples
    for i in range(3, isqrt(n),2):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False
    
    return sum(i for i in range(n) if is_prime[i])

# segemented sieve of eratosthenes (faster)
def compute(n):
    primes = [2, 3, 5, 7]
    end_segment = 1
    extend_at_most_n_segments_target = 10

    while primes[-1] < n:
        k = end_segment
        a = min(extend_at_most_n_segments_target, len(primes) - 1 - k)
        p, q = primes[k], primes[k + a]
        segment = range(p * p, q * q)
        segment_min = min(segment)
        segment_len = len(segment)
        is_prime = [True] * segment_len

        for i in range(k + a):
            pk = primes[i]
            start = segment_min + ((pk - (segment_min % pk)) % pk)
            is_prime[start - segment_min::pk] = repeat(False, len(range(start - segment_min, segment_len, pk)))

        primes.extend([x for x, is_prime in zip(segment, is_prime) if is_prime])
        end_segment += a
    
    return sum(primes[:bisect_right(primes,n)])

n = 2_000_000
print(f"Sum of All the Primes Below 2 Million Is: {compute(n)}")