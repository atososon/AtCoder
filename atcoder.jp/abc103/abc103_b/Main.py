s = input()
t = input()
for i in range(len(s)):
    x = s[i:] + s[:i]
    if x==t:
        print("Yes")
        break
    if i==len(s)-1:
        print("No")