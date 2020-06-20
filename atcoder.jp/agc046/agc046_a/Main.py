x = int(input())
count = x
ans = 1
while count%360!=0:
    count+=x
    ans+=1
print(ans)