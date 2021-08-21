import itertools

s, k = input().split()
k = int(k)
s = list(s)
s.sort()
ans = list(itertools.permutations(s, len(s)))
for i in range(len(ans)):
  ans[i] = "".join(ans[i])
ans = list(set(ans))
ans.sort()
print(ans[k-1])