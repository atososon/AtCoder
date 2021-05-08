from math import factorial

def combinations_count(n, r):
    if n < r:
        return 0
    else:
        return factorial(n) // (factorial(n - r) * factorial(r))

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i] % 200
ans = 0

for i in range(200):
    ans += combinations_count(a.count(i),2)
            
print(ans)
