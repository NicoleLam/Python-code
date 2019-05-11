'''
Input:
The first line contains an integer, n, denoting the number of elements in the array. 
The second line contains n space-separated integers describing the array's elements.

Output:
Print 3 lines of output in the following order:

The first line should be the value of first quartile ()
The second line should be the value of second quartile (), 
The third line should be the value of third quartile ().
'''

import statistics

n = int(input())
ls = sorted([int(x) for x in input().split()])
if n%2 == 0:
    lh = ls[:int(n/2)]
    uh = ls[int(n/2):]
else:
    lh = ls[:int(n/2)]
    uh = ls[int(n/2)+1:]

print(int(statistics.median(lh)))
print(int(statistics.median(ls)))
print(int(statistics.median(uh)))
