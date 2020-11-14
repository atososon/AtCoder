n = int(input())
a = list(map(int, input().split()))
ans1 = 3**n
ans2 = 1
for i in range(n):
    if a[i]%2 == 0:
        ans2 *= 2
ans = ans1 - ans2
print(ans)