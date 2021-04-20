a,b,c = map(int, input().split())
m = list()
s = a
while True:
    if s%b == c:
        print("YES")
        break
    if m.count(s%b) >= 1:
        print("NO")
        break
    m.append(s%b)
    s += a