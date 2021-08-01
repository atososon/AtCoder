import functools
import math

n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
  a[i] = abs(a[i]-x)
print(functools.reduce(math.gcd, a))