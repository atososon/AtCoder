x,k,d = map(int, input().split())
x = abs(x)
r = x//d
ans = 0
if r>k:
    ans = abs(x-k*d)
else:
    l = (k-r)%2
    if l==0:
        ans = abs(x-d*r)
    else:
        ans = abs(x-d*(r+1))
print(ans)