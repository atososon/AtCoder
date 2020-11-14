n = int(input())
s = list(input() for _ in range(n))
m = int(input())
t = list(input() for _ in range(m))
ans = 0
for i in range(n):
    ans = max(ans, s.count(s[i]) - t.count(s[i]))
print(ans)