n = int(input())
a1 = []
b1 = []
ab = []
for i in range(n):
  a,b = map(int, input().split())
  a1.append(a)
  b1.append(b)
  ab.append(a+b)
a2 = sorted(a1)
b2 = sorted(b1)
if a1.index(min(a1)) == b1.index(min(b1)):
  ans = min(max(a2[0], b2[1]), max(a2[1], b2[0]), min(ab))
else:
  ans = max(min(a1), min(b1))
print(ans)