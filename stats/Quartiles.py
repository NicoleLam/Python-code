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
