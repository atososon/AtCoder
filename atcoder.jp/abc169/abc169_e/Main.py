n = int(input())
a = []
b = []
for i in range(n):
    a1,b1 = map(int, input().split())
    a.append(a1)
    b.append(b1)
a.sort()
b.sort()
if n%2 == 1:
    print(b[(n+1)//2-1]-a[(n+1)//2-1]+1)
else:
	print(b[n//2-1]-a[n//2-1]+b[n//2]-a[n//2]+1)