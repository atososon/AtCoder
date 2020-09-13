a,b,c,d = map(int, input().split())
ans = max(a*c, a*d, b*c, b*d)
if ans<0 and (a<=0 and b>=0 or c<=0 and d>=0):
    ans = 0
print(ans)