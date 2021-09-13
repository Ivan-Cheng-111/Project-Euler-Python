""" Problem 14
Start: Sep/12/2021 5:50pm
Finished: Sep/13/2021 9:35pm
"""

from math import factorial, prod

# pascal triangle skip 2 rows per n, middle value is the number of possible routes
def compute4(n):
    n = n*2+1
    nums = [[1],[1,1]]
    tmp = []
    for _ in range(1,n-1):
        tmp.append(1)
        for j in range(len(nums[-1])-1):
            tmp.append(nums[-1][j]+nums[-1][j+1])
        tmp.append(1)
        nums.pop(0)
        nums.append(tmp)
        tmp = []
    return max(nums[-1])

# binomial coefficient formula but implemented differently
def compute3(n):
    paths = 1
    for i in range(n):
        paths *= 2*n - i
        paths //= i + 1
    return paths

# same as compute2
def compute2(n):
    a = prod(i for i in range(1,n*2+1))
    b = prod(i for i in range(1,n+1))
    return a//(b*b)

# binomial coefficient formula
def compute(n):
    return factorial(n*2)//(factorial(n)**2)

n = 20
print(f"The Number of Routes Through a {n}x{n} Grid Is: {compute(n)}")