""" Problem 28
Start: Sep/17/2021 11:35pm
Finished: Sep/18/2021 12:00am
"""

def compute(MAX):
	sum_of_diags = 1
	for n in range(3,MAX+1,2):
		# top-right n^2, top-left n^2-n+1, bot-left n^-2n+2, bot-right n^3n+3, sum all
		# 4n^2-6n+6
		sum_of_diags += 4*n*n - 6*n + 6
	return sum_of_diags

n = 1001
print(f"Sum of the Diagonal Numbers in a {n} by {n} Spiral Is: {compute(n)}")