h1,m1,h2,m2,k = map(int, input().split())
h = h2-h1
m = m2-m1
if m<0:
    m+=60
    h-=1
ans  = h*60+m-k
print(ans)