n = input()
p = int(n[0])
q = 0
c = n.count("9")
n1 = int(n)
while n1 >= 10:
    n1 //= 10
    q += 1
ans = 0
if c >= q and n[0]!="9" or q<1 or c>q:
    for i in range(len(n)):
        ans += int(n[i])
else:
    ans = (p-1) + 9 * q
print(ans)