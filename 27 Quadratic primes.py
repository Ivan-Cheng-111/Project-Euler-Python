""" Problem 27
Start: Sep/17/2021 10:50pm
Finished: Sep/17/2021 11:15pm
"""

from math import isqrt, prod

def is_prime(n) -> bool:
	if n < 2 or n % 2 == 0:
		return False
	elif n == 2:
		return True
	
	for i in range(2, isqrt(n)+1):
		if n % i == 0:
			return False
	return True

def compute():
	A_MAX = 999
	B_MAX = 1000
	
	# max_n=n max_vals=[a, b]
	max_n = 0
	max_vals = []

	for a in range(-A_MAX,A_MAX+1):
		for b in range(B_MAX+1):
			n = 0
			while is_prime(n*n+a*n+b):
				n += 1
				if n > max_n:
					max_n = n
					max_vals = [a,b]
	return prod(max_vals)

print(f"The Products of a b for the Quadratic Equation With the Most Number of Consecutive Primes Is: {compute()}")