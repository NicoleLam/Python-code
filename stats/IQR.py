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
