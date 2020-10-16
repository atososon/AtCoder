n = int(input())
a = list(map(int, input().split()))
ans = 0
f = 1
for i in range(n):
    if a[i]==f:
        f += 1
        continue
    else:
        ans += 1
if f==1:
    print("-1")
else:
    print(ans)