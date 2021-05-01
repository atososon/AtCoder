n, d1, h1 = map(int, input().split())
ans = 0
for i in range(n):
    d2, h2 = map(int, input().split())
    tmp = h2 - (h1-h2)/(d1-d2)*d2
    ans = max(ans, tmp)
if ans < 0:
    ans = 0.0
print(ans)
