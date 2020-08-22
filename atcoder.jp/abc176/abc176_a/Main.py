n,x,t = map(int,input().split())
ans = t
count = 1
while count*x < n:
    ans += t
    count += 1
print(ans)