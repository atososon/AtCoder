n, m = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for (j, i) in sorted(d):
    ans += j * min(i, m)
    m -= min(i, m)
print(ans)