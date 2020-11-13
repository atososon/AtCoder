n = int(input())
h = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if h[i-1] < h[i]:
        h[i] -= 1
    if h[i-1] > h[i]:
        ans = 1
if ans == 0:
    print("Yes")
else:
    print("No")