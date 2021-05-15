import itertools
import copy

s = input()
l1 = list()
l2 = list()
for i in range(10):
    if s[i] == "o":
        l1.append(i)
    elif s[i] == "?":
        l2.append(i)
ans = 0 

if len(l1) > 4:
    ans = 0
elif len(l1) == 4:
    ans = 24
else:
    al = itertools.combinations_with_replacement(l1+l2, 4-len(l1))
    for i in al:
        temp = copy.copy(l1)
        for j in i:
            temp.append(j)
        ans += len(set(itertools.permutations(temp)))
print(ans)
    