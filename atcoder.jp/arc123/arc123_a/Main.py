a = list(map(int, input().split()))
s1 = a[1] - a[0]
s2 = a[2] - a[1]
if s2 > s1:
    if abs(s2-s1)%2 == 0:
        ans = abs(s2-s1)//2
    else:
        ans = abs(s2-s1)//2 + 2
else:
    ans = abs(s1-s2)
print(ans)