n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0

for i in range(1,1001):
    f = 0
    for j in range(n):
        if i < a[j] or i > b[j]:
            f = 1
    if f == 0:
        ans += 1
print(ans)
