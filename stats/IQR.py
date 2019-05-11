'''
this code is for calculating IQR
The first line contains an integer n, denoting the number of elements in arrays 
The second line contains n space-separated integers describing the respective elements of array . 
The third line contains n space-separated integers describing the respective elements of array .

Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of  decimal place (i.e., format).
'''
import statistics 
n = int(input())
data = [int(x) for x in input().strip().split()]
freq = [int(x) for x in input().strip().split()]
s = []
for i in range(n):
    s += [data[i]] * freq[i]

N = len(s)
s = sorted(s)

if N%2 == 0:
    lh = s[:int(N/2)]
    uh = s[int(N/2):]
else:
    lh = s[:int(N/2)]
    uh = s[int(N/2)+1:]

print(round(float(statistics.median(uh) - statistics.median(lh)), 1))
