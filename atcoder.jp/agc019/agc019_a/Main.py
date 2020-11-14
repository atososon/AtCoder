q, h, s, d = map(int, input().split())
n = int(input())
m = min(q*4, h*2, s)
if m*2 <= d:
    ans = m*n
else:
    ans = n//2*d + n%2*m
print(ans)