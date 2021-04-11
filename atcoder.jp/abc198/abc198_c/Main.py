import math
r, x, y = map(int, input().split())
ans = math.ceil(((x**2+y**2) / r**2) ** 0.5)
if x**2+y**2 < r**2:
    ans = 2
if x**2+y**2 == r**2:
    ans = 1
print(ans)