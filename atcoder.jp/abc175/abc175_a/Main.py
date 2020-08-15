s = input()
ans1 = 0
ans = 0
for i in range(3):
    if s[i]=="R":
        ans1 += 1
    else:
        ans = ans1
        ans1 = 0
if not s=="RSS":
    print(max(ans,ans1))
else:
    print("1")