""" Problem 10
Start: Sep/10/2021 9:10pm
Finished: Sep/10/2021 9:45pm
"""

from itertools import repeat
from bisect import bisect_left

# sieve of eratosthenes
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
            start = segment_min + ((pk - (segment_min % pk) % pk))
            is_prime[start - segment_min::pk] = repeat(False, len(range(start - segment_min, segment_len, pk)))

        primes.extend([x for x, is_prime in zip(segment, is_prime) if is_prime])
        end_segment += a
    
    return sum(primes[:bisect_left(primes,n)])

n = 2_000_000
print(f"Sum of All the Primes Below 2 Million Is: {compute(n):,}")