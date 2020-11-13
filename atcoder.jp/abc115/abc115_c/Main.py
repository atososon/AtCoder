n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
ans = 999999999999999999999
for i in range(n-k+1):
    ans = min(ans, h[k+i-1]-h[i])
print(ans)