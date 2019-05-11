'''
Input:
The first line contains an integer n, denoting the number of elements in the array. 
The second line contains n space-separated integers describing the array's elements.

Output:
Print 3 lines of output in the following order:

Print the mean on a new line, to a scale of 1 decimal place 
Print the median on a new line, to a scale of 1 decimal place 
Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
'''
import numpy as np
from scipy import stats

_ = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))