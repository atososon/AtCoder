import math
n = int(input())
ans = [0 for _ in range(10001)]

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            t = x**2 + y**2 + z**2 + x*y + y*z + z*x 
            if t <= 10000:
                ans[t] += 1
for i in range(1,n+1):
    print(ans[i])