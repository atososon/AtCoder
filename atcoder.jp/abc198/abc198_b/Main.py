n = input()
f = 0
for i in range(11):
    n1 = "0"*i + n
    if n1 == n1[::-1]:
        f = 1
 
if f == 1:
    print("Yes")
else:
    print("No")