n, m = map(int, input().split())
ac = [0] * n
wa = [0] * n
for i in range(m):
    p, s = input().split()
    p = int(p)-1
    if s == "AC":
        ac[p] = 1
    else:
        if ac[p] == 0:
            wa[p] += 1
waa = 0
for i in range(n):
    if ac[i] == 1:
        waa += wa[i]
print(sum(ac), waa)