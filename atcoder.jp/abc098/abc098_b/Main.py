n = int(input())
s = input()
ans = 0
for i in range(1,len(s)-1):
    tmp = 0
    for st in set(s[:i]):
        if s[i:].count(st) > 0:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
