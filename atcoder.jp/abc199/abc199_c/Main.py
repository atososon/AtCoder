n = int(input())
s = input()
q = int(input())
f = 0
s = list(s)
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if f == 0:
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            s[a-1-n], s[b-1-n] = s[b-1-n], s[a-1-n]
    else:
        if f == 0:
            f = 1
        else:
            f = 0
if f == 1:
    s = s[n:] + s[:n]
print("".join(s))
