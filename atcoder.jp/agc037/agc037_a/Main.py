s = input()
ans = []
i = 0
j = 1
while j <= len(s):
    if len(ans) > 0:
        if s[i:j] != ans[-1]:
            ans.append(s[i:j])
            i = j
            j += 1
        else:
            j += 1
    else:
        ans.append(s[i:j])
        i = j
        j += 1
print(len(ans))