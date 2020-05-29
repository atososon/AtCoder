h = int(input())
ans = 1
count = 1
while h>1:
    h//=2
    count = count*2
    ans += count
print(ans)