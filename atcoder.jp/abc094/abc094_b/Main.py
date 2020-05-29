n,m,x = map(int, input().split())
a = list(map(int, input().split()))
s = x
cost = 0
while s!=0:
    s-=1
    if s in a:
        cost+=1
ans = cost
cost = 0
s = x
while s!=n:
    s+=1
    if s in a:
        cost+=1 
ans = min(ans,cost)
print(ans)