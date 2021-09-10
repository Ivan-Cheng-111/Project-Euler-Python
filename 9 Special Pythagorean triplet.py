""" Problem 9
Start: Sep/10/2021 4:40pm
Finished: Sep/10/2021 8:30pm
"""

def compute(n):
    # check all possible values of abc until n//2
    for a in range(1,n//2):
        for b in range(a+1,n//2):
            c=n-a-b
            if a*a+b*b == c*c:
                return a*b*c

n = 1000
print(f"The Product of `abc` Such That `a^2+b^2=c^2` Given `a+b+c={n}` Is: {compute(n)}")