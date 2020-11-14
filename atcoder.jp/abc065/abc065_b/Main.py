n = int(input())
a = list(int(input()) for _ in range(n))
i = 0
c = 0
while c <= n+1:
    c += 1
    i = a[i]-1
    if i == 1:
        print(c)
        break
if c == n+2:
    print("-1")