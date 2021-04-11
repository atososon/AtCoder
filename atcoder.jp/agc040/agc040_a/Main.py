s = input()
ans = [0] * (len(s)+1)

for i in range(len(s)):
    if s[i] == "<":
        ans[i+1] = ans[i] + 1

for i in reversed(range(len(s))):
    if s[i] == ">":
        ans[i] = max(ans[i+1]+1, ans[i])

print(sum(ans))