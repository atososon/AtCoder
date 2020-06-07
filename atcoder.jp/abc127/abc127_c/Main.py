n,m = map(int, input().split())
L = 0
R = 100000
for i in range(m):
    l,r = map(int, input().split())
    L = max(L,l)
    R = min(R,r)
if R - L < 0:
    ans = 0
else:
    ans = R - L + 1
print(ans)