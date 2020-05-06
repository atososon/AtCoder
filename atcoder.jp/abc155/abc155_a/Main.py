a,b,c=(int(x) for x in input().split())
if a==b==c or a!=b!=c!=a:
    print("No")
else:
    print("Yes")