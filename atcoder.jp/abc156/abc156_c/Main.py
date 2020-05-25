n = int(input())
x = list(map(int,input().split()))
ans2 = 99999999999999
for i in range(100):
    ans1=0
    for j in range(n):
        ans1 += pow(x[j]-i,2)
    ans2 = min(ans2,ans1)
print(ans2)