import math
def prime(num):
    if num ==1 :
        return "Not prime"
    elif num == 2:
        return "Prime"
    else:
        n = int(math.sqrt(num))
        for i in range(2,n+1):
            if num%i ==0:
                return "Not prime"
        return "Prime"

T = int(input())
for i in range(T):
    print(prime(int(input())))
