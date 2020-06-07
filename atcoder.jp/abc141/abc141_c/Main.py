n,k,q = map(int, input().split())
a = [int(input()) for _ in range(q)]
ans = [0 for _ in range(n)]
for i in range(q):
    ans[a[i]-1] += 1
for i in range(n):
    if q-ans[i] < k:
        print("Yes")
    else:
        print("No")