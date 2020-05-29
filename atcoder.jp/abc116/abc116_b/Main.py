s = int(input())
a = []
a.append(s)
ans = 0
while True:
    if a[ans]%2==0:
        if a[ans]//2 in a:
            print(ans+2)
            break
        a.append(a[ans]//2)
    else :
        if 3*a[ans]+1 in a:
            print(ans+2)
            break
        a.append(3*a[ans]+1)
    ans+=1