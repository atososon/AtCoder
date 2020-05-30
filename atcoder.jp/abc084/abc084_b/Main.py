a,b = map(int, input().split())
s = input()
f = 0
for i in range(a):
    if s[i]=="-":
        f = 1
if s[a]!="-":
    f = 1
for i in range(a+1,a+b+1):
    if s[i]=="-":
        f = 1
if f==0:
    print("Yes")
else:
    print("No")