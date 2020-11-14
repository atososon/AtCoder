n = int(input())
a = list(map(int, input().split()))
ans = 2020202020
s = sum(a)
m = 0
for i in range(n-1):
    m += a[i]
    ans = min(ans, abs(s - 2*m))
print(ans)