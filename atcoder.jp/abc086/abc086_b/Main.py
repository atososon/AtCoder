import math
a,b = input().split()
f = int(a+b)
if math.sqrt(f)%1 == 0:
    print("Yes")
else:
    print("No")