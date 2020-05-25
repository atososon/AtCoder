a,b = map(int,input().split())
ans = 0
while True:
    if ans*(a-1)+1>=b:
        break
    ans+=1
print(ans)