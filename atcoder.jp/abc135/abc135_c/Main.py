n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a[i] > 0:
        if b[i] >= a[i]:
            b[i] -= a[i]
            ans += a[i]
            a[i] = 0
        else:
            a[i] -= b[i]
            ans += b[i]
            b[i] = 0
    if b[i] > 0:
        if a[i+1] > 0:
            if b[i] >= a[i+1]:
                b[i] -= a[i+1]
                ans += a[i+1]
                a[i+1] = 0
            else:
                a[i+1] -= b[i]
                ans += b[i]
                b[i] = 0
print(ans)