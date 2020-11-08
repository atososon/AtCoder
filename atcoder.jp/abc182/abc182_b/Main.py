n = int(input())
a = list(map(int, input().split()))
ans = {}
for i in range(2,1001):
    k = i
    ans2 = 0
    for j in range(n):
        if a[j]%k == 0:
            ans2 += 1
    ans[ans2] = k
ans_sorted = sorted(ans.items(), key=lambda x:x[0])
print(ans_sorted[-1][1])