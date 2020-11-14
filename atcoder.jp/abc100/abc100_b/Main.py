d, n = map(int, input().split())
ans = 100**d*n
if n == 100:
    ans = 100**d*101
print(ans)