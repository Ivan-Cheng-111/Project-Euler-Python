""" Problem 29
Start: Sep/18/2021 12:55am
Finished: Sep/18/2021 1:00am
"""

def compute(a_max,b_max):
	terms = set()
	for a in range(2,a_max+1):
		for b in range(2,b_max+1):
			terms.add(a**b)
	return len(terms)

a_max, b_max = 100, 100
print(f"The Number of Distinct Terms in Sequence a^b for a,b Max {a_max},{b_max} Is: {compute(a_max,b_max)}")