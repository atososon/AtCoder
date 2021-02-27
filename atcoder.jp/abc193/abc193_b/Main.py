n = int(input())
ans = 10 ** 10
for i in range(n):
    a, p, x = map(int, input().split())
    z = x - (a+0.5)//1.0
    if z >= 1:
        ans = min(ans, p)

if ans == 10**10:
    print("-1")
else:
    print(ans)
    