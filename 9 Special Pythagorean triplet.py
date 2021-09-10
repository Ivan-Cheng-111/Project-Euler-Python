""" Problem 7
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

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