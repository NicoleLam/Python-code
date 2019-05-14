'''
A manufacturer of metal pistons finds that, on average, 12% of the 
pistons they manufacture are rejected because they are incorrectly 
sized. What is the probability that a batch of  pistons will contain:

1. No more than  rejects?
2. At least  rejects?
'''

import math
def comb(n,x):
    return math.factorial(n)/(math.factorial(x)*math.factorial(n-x))

def prob(n,x,p):
    return comb(n,x)*p**x*(1-p)**(n-x)

print(round(sum([prob(10,i,0.12) for i in range(0,3)]),3))
print(round(1-sum([prob(10,i,0.12) for i in range(0,2)]),3))
