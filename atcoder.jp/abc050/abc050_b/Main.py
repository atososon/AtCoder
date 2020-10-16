n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = []
x = []
for i in range(m):
    pi, xi = map(int, input().split())
    p.append(pi)
    x.append(xi)
for i in range(m):
    ans = sum(t) - t[p[i]-1] + x[i]
    print(ans)    