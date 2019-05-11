import math

n = int(input())

data = [int(x) for x in input().strip().split()]
m = sum(data)/n
va = sum([((x - m) ** 2) for x in data]) / n
print(round(math.sqrt(va),1))