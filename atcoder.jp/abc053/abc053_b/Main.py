import re
s = input()
ans = re.search(r'A.*Z', s)
print(len(ans.group()))