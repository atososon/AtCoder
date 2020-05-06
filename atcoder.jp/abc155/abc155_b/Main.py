n=int(input())
a=list(map(int,input().split()))
f=1
for i in range(n):
    if a[i]%2==0 and a[i]%3!=0 and a[i]%5!=0:
        f=0
        break
if f==1:
    print("APPROVED")
else:
    print("DENIED")