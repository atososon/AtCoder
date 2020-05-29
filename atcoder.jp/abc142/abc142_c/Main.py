n = int(input())
a = list(map(int, input().split()))
ans = {}
ans = {a[i]:i for i in range(n)}
for i in range(1,n+1):
    print(ans[i]+1,end=" ")
print()