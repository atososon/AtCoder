n, s, d = map(int, input().split())
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    if x<s and y>d:
        ans = 1
if ans == 0:
    print("No")
else:
    print("Yes")