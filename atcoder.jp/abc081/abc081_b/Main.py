n = int(input())
a = list(map(int, input().split()))
ans = 0
f = 0
while f == 0:
    for i in range(n):
        if a[i]%2==0:
            a[i]//=2
        else:
            print(ans)
            f = 1
            break
    ans+=1