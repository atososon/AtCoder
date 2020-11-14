s = input()
k = int(input())
not_1 = 0
for i in range(len(s)):
    if s[i] == "1":
        not_1 += 1
    else:
        break
if k-1 < not_1:
    print(s[k-1])
else:
    print(s[not_1])