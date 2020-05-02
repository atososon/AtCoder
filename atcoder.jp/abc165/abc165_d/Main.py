a,b,n=(int(x) for x in input().split())
n = min(b-1,n)
print((a*n)//b-a*(n//b))