n = int(input())
u = []
v = []
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    u.append(x+y)
    v.append(x-y)
ans = max(max(u) - min(u), max(v) - min(v))
print(ans)