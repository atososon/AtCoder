n = int(input())
p = list(map(int, input().split()))
s = list([False]*200001)
ans = 0
for i in range(n):
    s[p[i]] = True
    while s[ans]:
        ans += 1
    print(ans)