n = int(input())
h = list(map(int, input().split()))
ans = 0
m = 0
for i in range(n-1):
    if h[i] >= h[i+1]:
        m += 1
        ans = max(ans, m)
    else:
        ans = max(ans, m)
        m = 0
print(ans)