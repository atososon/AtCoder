n = int(input())
a = list(list(map(int, input().split())) for _ in range(2))
ans = 0
for i in range(n):
    ans = max(ans, sum(a[0][:i+1]) + sum(a[1][i:]))
print(ans)