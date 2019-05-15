'''
The ratio of boys to girls for babies born in Russia is 1.09:1. 
If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
'''
import math
p = 1.09/2.09
def comb(n,x):
    return math.factorial(n)/((math.factorial(x)*math.factorial(n-x)))

def prob(n,x,p):
    return comb(n,x)*p**x*(1-p)**(n-x)
result = 0
for i in range(3,7):
    result += prob(6,i,p)

print(round(result,3))