MOD = 360
 
n = int(input())
a = list(map(int, input().split()))
s = 0
l = list()
for i in a:
  s += i
  s %= MOD
  l.append(s)
l.sort()
ans = l[0]
for i in range(0, len(l)-1):
  ans = max(ans, l[i+1] - l[i])
ans = max(ans, 360-l[-1])
print(ans)