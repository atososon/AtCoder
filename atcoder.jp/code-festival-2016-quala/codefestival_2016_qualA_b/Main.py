n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i == a[a[i]-1]-1:
        ans += 1
ans //= 2
print(ans)