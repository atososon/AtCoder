s = input()
t = input()
ans = 0
for i in range(len(s)-len(t)+1):
    m = 0
    for j, k in zip(s[i:],t):
        if j==k:
            m += 1
    if m > ans:
        ans = m
print(len(t) - ans)