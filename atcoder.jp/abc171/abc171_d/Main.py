from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = []
c = []
s = []

ans = sum(a)
s = Counter(a)
for i in range(q):
    bi,ci = map(int, input().split())
    b.append(bi)
    c.append(ci)
for i in range(q):
    ans += s[b[i]] * (c[i]-b[i])
    s[c[i]] += s[b[i]]
    s[b[i]] = 0
    print(ans)