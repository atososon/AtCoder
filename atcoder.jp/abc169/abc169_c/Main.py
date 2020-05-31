a,b = map(str,input().split())
a1 = int(a)
b1 = int(float(b)*1000)
ab = a1*b1
ans = int(ab//1000)
print(ans)